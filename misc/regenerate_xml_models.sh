# The Schema files (xsd) can be found [here](https://www.entsoe.eu/publications/electronic-data-interchange-edi-library/) under the "EIC data exchange" section.
# Put them into a folder (e.g. ./xsd/) and run

xsdata generate ./xsd/ --relative-imports --package  xml_models
mv xml_models src/entsoe/xml_models/
