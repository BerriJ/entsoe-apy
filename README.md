# entsoe-api-py

The Schema files (xcd) can be found [here](https://www.entsoe.eu/publications/electronic-data-interchange-edi-library/) under the "EIC data exchange" section.

```shell
xsdata generate ./CIM_2025-07-03/ --relative-imports --package  xml_models
mv xml_models src/entsoe_api_py/xml_models/
```

After that, update the created modules with a replace all so that the imports look like this:

```python
from entsoe_api_py.xml_models.{...}
```
