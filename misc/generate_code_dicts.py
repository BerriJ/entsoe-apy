# %%
import xml.etree.ElementTree as ET

# Load the XSD
file_path = "urn-entsoe-eu-wgedi-codelists.xsd"
tree = ET.parse(file_path)
root = tree.getroot()

ns = {"xs": "http://www.w3.org/2001/XMLSchema"}

enum_classes_fixed = []

for simple_type in root.findall("xs:simpleType", ns):
    type_name = simple_type.attrib.get("name")
    restriction = simple_type.find("xs:restriction", ns)
    if restriction is None:
        continue

    enums = []
    for enum in restriction.findall("xs:enumeration", ns):
        code = enum.attrib.get("value")
        title = None

        # find Title under documentation
        doc = enum.find("xs:annotation/xs:documentation", ns)
        if doc is not None:
            title_elem = doc.find(".//Title")
            if title_elem is not None and title_elem.text:
                title = title_elem.text.strip()

        if not title:
            title = code  # fallback

        enums.append((code, title))

    if enums:
        lines = [f"class {type_name}(Enum):"]
        for code, title in enums:
            identifier = code.replace("-", "_").replace(" ", "_")
            if identifier[0].isdigit():
                identifier = "_" + identifier
            lines.append(f'    {identifier} = "{title}"')
        enum_classes_fixed.append("\n".join(lines))

# Write all enum classes to a file
output_file = (
    "/home/jonathan/git/DSEE/database/code/entsoe-apy/src/entsoe/utils/codes.py"
)

with open(output_file, "w") as f:
    f.write("from enum import Enum\n\n")
    f.write("\n\n".join(enum_classes_fixed))
