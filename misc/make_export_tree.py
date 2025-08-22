import importlib
import pkgutil


def get_module_exports(module_name, max_depth=3, current_depth=0):
    """Recursively get all exports from a module and its submodules"""
    if current_depth >= max_depth:
        return {}

    try:
        module = importlib.import_module(module_name)
        exports = {}

        # Get direct exports
        if hasattr(module, "__all__"):
            direct_exports = module.__all__
        else:
            direct_exports = [name for name in dir(module) if not name.startswith("_")]

        # Filter to actual exportable objects
        actual_exports = []
        for name in direct_exports:
            try:
                obj = getattr(module, name)
                obj_type = type(obj).__name__
                # Include functions, classes, and constants, but not modules
                # unless explicitly needed
                if obj_type in [
                    "function",
                    "type",
                    "str",
                    "int",
                    "float",
                    "dict",
                    "list",
                ] or callable(obj):
                    actual_exports.append((name, obj_type))
                elif (
                    hasattr(obj, "__module__")
                    and obj.__module__
                    and obj.__module__.startswith("entsoe")
                ):
                    actual_exports.append((name, obj_type))
            except Exception:
                pass

        exports["_direct"] = actual_exports

        # Get submodule exports
        try:
            if hasattr(module, "__path__"):
                for _, name, ispkg in pkgutil.iter_modules(
                    module.__path__, module_name + "."
                ):
                    if not name.endswith(".__pycache__"):
                        submodule_name = name.split(".")[-1]
                        try:
                            subexports = get_module_exports(
                                name, max_depth, current_depth + 1
                            )
                            if subexports:
                                exports[submodule_name] = subexports
                        except Exception as e:
                            exports[submodule_name] = f"Error: {str(e)[:50]}"
        except Exception:
            pass

        return exports

    except Exception as e:
        return f"Error importing {module_name}: {str(e)[:50]}"


def print_tree(exports, indent=0, max_items_per_level=20, file=None):
    """Print the export tree in a nice format"""
    prefix = "  " * indent

    if isinstance(exports, str):
        print(f"{prefix}└── {exports}", file=file)
        return

    if isinstance(exports, dict):
        items = list(exports.items())

        # Handle direct exports first
        if "_direct" in exports:
            direct = exports["_direct"]
            if direct:
                print(f"{prefix}├── Direct exports ({len(direct)} items):", file=file)
                for i, (name, obj_type) in enumerate(direct[:max_items_per_level]):
                    marker = (
                        "├──"
                        if i < min(len(direct), max_items_per_level) - 1
                        else "└──"
                    )
                    print(f"{prefix}│   {marker} {name} ({obj_type})", file=file)
                if len(direct) > max_items_per_level:
                    print(
                        f"{prefix}│   └── ... and "
                        f"{len(direct) - max_items_per_level} more",
                        file=file,
                    )
                print(f"{prefix}│", file=file)

            # Remove _direct from items to process
            items = [(k, v) for k, v in items if k != "_direct"]

        # Handle submodules
        for i, (key, value) in enumerate(items):
            is_last = i == len(items) - 1
            marker = "└──" if is_last else "├──"

            if isinstance(value, dict) and value:
                print(f"{prefix}{marker} {key}/", file=file)
                print_tree(value, indent + 1, max_items_per_level, file=file)
            elif isinstance(value, str):
                print(f"{prefix}{marker} {key}: {value}", file=file)
            else:
                print(f"{prefix}{marker} {key}", file=file)


print("ENTSOE Module Export Tree")
print("=" * 50)
exports = get_module_exports("entsoe", max_depth=2)

# Write tree to a markdown file
with open("./docs/entsoe_export_tree.md", "w") as f:
    print("# ENTSOE Module Export Tree", file=f)
    print("", file=f)
    print(
        "A comprehensive overview of all exported classes, functions, "
        "and modules in the entsoe-api-py package.",
        file=f,
    )
    print(
        "This tree shows the hierarchical structure of the package "
        "with direct exports and submodules.",
        file=f,
    )
    print("", file=f)
    print("```", file=f)
    print_tree(exports, file=f)
    print("```", file=f)
