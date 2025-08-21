from .config import EntsoEConfig, get_config, has_config, reset_config, set_config
from .mappings_dict import mappings
from .query_api import query_api

# Initialize global configuration on import
# This will attempt to get the security token from ENTSOE_API environment variable
set_config()


__all__ = [
    "query_api",
    "mappings",
    "EntsoEConfig",
    "set_config",
    "get_config",
    "has_config",
    "reset_config",
]
