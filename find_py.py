import re
import sys
from pathlib import Path
from xml.etree import ElementTree as ET

NAMESPACE_PATTERN = re.compile(
    r"^urn:iec62325\.351:tc57wg16:(?P<section>451-\d+):(?P<doc>[^:]+):(?P<major>\d+):(?P<minor>\d+)$"
)

FILE_PATTERN = re.compile(
    r"^iec62325_(?P<section>\d+_\d+)_(?P<name>[a-z0-9_]+)_v(?P<major>\d+)_(?P<minor>\d+)\.py$"
)


def extract_namespace(xml_path: Path) -> str:
    tree = ET.parse(xml_path)
    root = tree.getroot()
    if root.tag[0] == "{":
        return root.tag[1:].split("}")[0]
    raise ValueError("No default namespace found in root element")


def normalize_doc_token(doc_token: str) -> str:
    # Keep original plus variants for matching
    variants = {doc_token}
    # If ends with 'document' keep stripped
    if doc_token.endswith("document"):
        variants.add(doc_token[:-8])  # remove 'document'
    # Also add underscore stripped variant
    variants.add(doc_token.replace("_", ""))
    # For each variant add versions with/without 'document'
    extended = set()
    for v in variants:
        extended.add(v)
        extended.add(v + "document")
    return variants.union(extended)


def find_matching_file(
    models_dir: Path, section: str, doc_token: str, major: str, minor: str
) -> Path | None:
    wanted_variants = normalize_doc_token(doc_token)
    # Convert section 451-3 to 451_3 for filenames
    section_file = section.replace("-", "_")
    candidates = []
    for fp in models_dir.iterdir():
        if not fp.is_file():
            continue
        m = FILE_PATTERN.match(fp.name)
        if not m:
            continue
        if m.group("section") != section_file:
            continue
        if m.group("major") != major or m.group("minor") != minor:
            continue
        name_part = m.group("name")
        # Build comparable variants for file name
        file_variants = {
            name_part,
            name_part.replace("_", ""),
            name_part + "document",
            name_part.replace("_", "") + "document",
        }
        if file_variants & wanted_variants:
            candidates.append(fp)

    if not candidates:
        return None

    # If multiple, prefer exact (without added 'document') match
    def rank(fp: Path):
        name_part = FILE_PATTERN.match(fp.name).group("name")
        if doc_token == name_part:
            return 0
        if doc_token == name_part + "document":
            return 1
        return 2

    candidates.sort(key=rank)
    return candidates[0]


def find_model(xml_path: Path, models_dir: Path) -> Path:
    ns = extract_namespace(xml_path)
    m = NAMESPACE_PATTERN.match(ns)
    if not m:
        raise ValueError(f"Namespace not recognized pattern: {ns}")
    section = m.group("section")
    doc_token = m.group("doc").lower()
    major = m.group("major")
    minor = m.group("minor")
    match = find_matching_file(models_dir, section, doc_token, major, minor)
    if not match:
        raise FileNotFoundError(
            f"No model file found for {section=} {doc_token=} v{major}_{minor} in {models_dir}"
        )
    return match


def main(argv=None):
    argv = argv or sys.argv[1:]
    if len(argv) < 2:
        print(
            "Usage: python find_model_for_xml.py <xml_file> <models_dir>",
            file=sys.stderr,
        )
        sys.exit(1)
    xml_path = Path(argv[0]).resolve()
    models_dir = Path(argv[1]).resolve()
    model = find_model(xml_path, models_dir)
    print(model)


if __name__ == "__main__":
    main()
