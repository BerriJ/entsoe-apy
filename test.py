# %%
from os import getenv
from xml.etree import ElementTree as ET
import inspect

from httpx import get
from xsdata.formats.dataclass.parsers import XmlParser

import entsoe_api_py.xml_models as xmlm

_ENTSOE_API = getenv("ENTSOE_API")
assert _ENTSOE_API is not None

EIC = "10Y1001A1001A82H"
documentType = "A44"
processType = "A16"

period_start = 202012312300
period_end = 202101022300

URL = f"https://web-api.tp.entsoe.eu/api?documentType={documentType}&in_Domain={EIC}&out_Domain={EIC}&securityToken={_ENTSOE_API}&periodStart={period_start}&periodEnd={period_end}&contract_MarketAgreement.type=A01"
TIME_OUT_SECONDS = 60


response = get(URL, timeout=TIME_OUT_SECONDS)


def extract_namespace_and_find_classes(response) -> tuple[str, type]:
    root = ET.fromstring(response.text)
    if root.tag[0] == "{":
        namespace = root.tag[1:].split("}")[0]
    else:
        raise ValueError("No default namespace found in root element")

    if not namespace:
        raise ValueError("Empty namespace found in root element")

    matching_classes = []

    # Get all classes from the xmlm module
    for name, obj in inspect.getmembers(xmlm, inspect.isclass):
        if (
            hasattr(obj, "__dataclass_fields__")
            and hasattr(obj, "Meta")
            and hasattr(obj.Meta, "namespace")
        ):
            if obj.Meta.namespace == namespace:
                matching_classes.append((name, obj))

    if len(matching_classes) == 0:
        raise ValueError(f"No classes found matching namespace '{namespace}'")
    elif len(matching_classes) > 1:
        class_names = [name for name, _ in matching_classes]
        raise ValueError(
            f"Multiple classes found matching namespace '{namespace}': {class_names}"
        )
    return namespace, matching_classes[0][1]


namespace, matching_class = extract_namespace_and_find_classes(response)


# %%

result: matching_class = XmlParser().from_string(response.text, matching_class)
print(result.time_series[0])
# %%
