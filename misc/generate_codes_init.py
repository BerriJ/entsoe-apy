#!/usr/bin/env python3
"""Generate __init__.py for the codes module by extracting all enums from codes.py."""

from pathlib import Path
import re


def extract_class_names(codes_file: Path) -> list[str]:
    """Extract all class names from codes.py."""
    class_names = []
    with open(codes_file, "r") as f:
        for line in f:
            # Match all class definitions
            match = re.match(r"^class (\w+)\(", line)
            if match:
                class_names.append(match.group(1))
    return sorted(class_names)


def generate_init_file(class_names: list[str], output_file: Path) -> None:
    """Generate the __init__.py file with all the exports."""
    # Create the import statement
    imports = "from .codes import (\n"
    imports += ",\n".join(f"    {name}" for name in class_names)
    imports += ",\n)"

    # Create the __all__ list
    all_list = "__all__ = [\n"
    all_list += ",\n".join(f'    "{name}"' for name in class_names)
    all_list += ",\n]"

    # Combine everything
    content = f'''"""ENTSO-E API Code enumerations.

This module exports all the standard code enumerations used by the ENTSO-E API
for various parameters and data types.
"""

{imports}

{all_list}
'''

    with open(output_file, "w") as f:
        f.write(content)

    print(f"Generated {output_file} with {len(class_names)} exports:")
    for name in class_names:
        print(f"  - {name}")


def main():
    # Determine paths
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    codes_file = repo_root / "src" / "entsoe" / "codes" / "codes.py"
    init_file = repo_root / "src" / "entsoe" / "codes" / "__init__.py"

    if not codes_file.exists():
        print(f"Error: {codes_file} not found")
        return 1

    # Extract class names
    class_names = extract_class_names(codes_file)

    if not class_names:
        print("Error: No classes found in codes.py")
        return 1

    # Generate __init__.py
    generate_init_file(class_names, init_file)
    print(f"\nSuccessfully generated {init_file}")
    return 0


if __name__ == "__main__":
    exit(main())
