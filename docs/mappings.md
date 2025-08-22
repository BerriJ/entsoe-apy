## EIC Mappings Dictionary

All queries must be made using "EIC" codes. The below mappings can be used, for example, to query Prices for all Biddingzones (BZN), Countries (CTY), Control Areas (CTA) etc. The mappings were created on (2025-08-15) using the [official documentation](https://transparencyplatform.zendesk.com/hc/en-us/articles/15885757676308-Area-List-with-Energy-Identification-Code-EIC).

Two changes were made:

- `CTY` was added as an identifier for countries, as they did not have one before.
- Some country names where replaced by their short codes ("Azerbaijan (AZ)" -> "AZ") to merge certain concise entries in the dict, like the one for Azerbaijan which is a Biddingzone, Control Area and Country at the same time.

::: entsoe.utils.mappings