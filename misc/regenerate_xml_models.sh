#!/bin/sh

echo "Downloading XSD files..."
python3 misc/download_xsd.py
echo "Extracting XSD files..."
python3 misc/extract_all_xsd.py

echo "Regenerating XML models..."
xsdata generate ./xsd/ --relative-imports --package xml_models --output pydantic

echo "Copying XML models to src/entsoe/ ..."
cp -R xml_models src/entsoe/
echo "Cleaning up..."
rm -R xml_models

echo "Regenerating code dictionaries..."
python3 misc/generate_code_dicts.py
echo "Regenerating codes __init__.py ..."
python3 misc/generate_codes_init.py

# Ruff
ruff format src/

echo "Regeneration complete."