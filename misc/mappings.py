# %%
import csv

# Source: https://transparencyplatform.zendesk.com/hc/en-us/articles/15885757676308-Area-List-with-Energy-Identification-Code-EIC

# This script reads EIC codes from a CSV file and converts them into a nested
# dictionary format. To update just copy the table from entsoe into the csv file
# (eic_codes.csv) e.g. with libreoffice calc and run this script from the root
# of this repository: python3 ./misc/mappings.py


def read_eic_codes_csv(file_path="./misc/eic_codes.csv"):
    """
    Read EIC codes CSV file while preserving line breaks in the second column.

    Args:
        file_path (str): Path to the eic_codes.csv file

    Returns:
        list: List of rows with preserved formatting
    """
    with open(file_path, "r", encoding="utf-8", newline="") as file:
        # Use csv.reader with quoting to handle embedded newlines
        reader = csv.reader(file, quotechar='"', quoting=csv.QUOTE_ALL)
        rows = list(reader)

    return rows


def convert_csv_list_to_dict(csv_rows, key_column=0, value_column=1):
    """
    Convert CSV list data to dictionary format with values as dictionaries split by "|".

    Args:
        csv_rows (list): List of rows from CSV reader
        key_column (int): Index of column to use as keys (default: 0)
        value_column (int): Index of column to use as values (default: 1)

    Returns:
        dict: Dictionary with keys from first column and values as dictionaries split by "|"
    """
    if not csv_rows:
        return {}

    # Skip header row if it exists
    data_rows = csv_rows[1:] if csv_rows and len(csv_rows) > 1 else csv_rows

    result_dict = {}
    for row in data_rows:
        if len(row) > max(key_column, value_column):
            key = row[key_column]
            value = row[value_column]
            # Split value by newlines and convert to list
            value_list = [item.strip() for item in value.split("\n") if item.strip()]
            # Check each element and prepend "CTY|" if it doesn't contain "|"
            value_list = [item if "|" in item else f"CTY|{item}" for item in value_list]
            # Split each element by "|" and convert to dictionary (inverted: value|key)
            value_dict = {}
            for item in value_list:
                if "|" in item:
                    parts = item.split("|", 1)  # Split only on first "|"
                    if len(parts) == 2:
                        # Inverted: value becomes key, collect keys into lists
                        if parts[1] not in value_dict:
                            value_dict[parts[1]] = []
                        value_dict[parts[1]].append(parts[0])
            result_dict[key] = value_dict

    return result_dict


def consolidate_cty_entries(mappings_dict):
    """
    Consolidate CTY entries by moving them to their corresponding country code keys
    when the CTY value contains the country code in brackets.

    Args:
        mappings_dict (dict): Nested dictionary with EIC codes as outer keys

    Returns:
        dict: Updated dictionary with consolidated CTY entries
    """
    consolidated_dict = {}

    for eic_code, country_dict in mappings_dict.items():
        new_country_dict = country_dict.copy()

        # Look for CTY entries that contain country codes in brackets
        cty_entries_to_remove = []
        for key, prefix_list in country_dict.items():
            if "CTY" in prefix_list:
                # Check if this key contains a country code in brackets
                if "(" in key and ")" in key:
                    # Extract country code from brackets
                    start = key.find("(") + 1
                    end = key.find(")")
                    country_code = key[start:end]

                    # If this country code exists as a separate key, merge CTY into it
                    if country_code in country_dict:
                        new_country_dict[country_code].extend(["CTY"])
                        # Remove duplicates
                        new_country_dict[country_code] = list(
                            set(new_country_dict[country_code])
                        )
                        # Mark this CTY entry for removal
                        cty_entries_to_remove.append(key)

        # Remove the consolidated CTY entries
        for key in cty_entries_to_remove:
            if key in new_country_dict:
                del new_country_dict[key]

        consolidated_dict[eic_code] = new_country_dict

    return consolidated_dict


# Write the consolidated mappings dictionary to a new file
def write_mappings_to_file(mappings_dict, output_file="mappings_dict.py"):
    """
    Write the mappings dictionary to a Python file as a variable assignment.

    Args:
        mappings_dict (dict): The mappings dictionary to write
        output_file (str): Output filename
    """
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("# Auto-generated mappings dictionary\n")
        f.write("# Refer to mappings.py for more details\n")
        f.write("# EIC code mappings with country codes and prefixes\n\n")
        f.write("mappings = ")
        f.write(repr(mappings_dict))
        f.write("\n")


# Read the EIC codes CSV file
mappings_dict = convert_csv_list_to_dict(read_eic_codes_csv())

# Apply consolidation to mappings_dict
mappings_consolidated = consolidate_cty_entries(mappings_dict)

# Write the consolidated mappings to file
write_mappings_to_file(mappings_consolidated, "./src/entsoe_api_py/mappings_dict.py")
# %%
