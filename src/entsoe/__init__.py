from .config.config import set_config

# Initialize global configuration on import
# This will attempt to get the security token from ENTSOE_API environment variable
set_config()
