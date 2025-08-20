#!/usr/bin/env python3
"""
Postman Collection Processing Script

This script processes the Entso-e Transparency Platform Restful API Postman collection:
1. Removes response fields from the original collection
2. Filters to keep only specific API groups
3. Creates a cleaned final collection
4. Splits each group into separate collection files

Usage:
    python strip_json.py
"""

import json
import os


def remove_key(obj, key_to_remove):
    """
    Recursively remove a specific key from a nested dictionary/list structure.

    Args:
        obj: The object to process (dict, list, or other)
        key_to_remove: The key to remove from dictionaries

    Returns:
        The processed object with the specified key removed
    """
    if isinstance(obj, dict):
        return {
            k: remove_key(v, key_to_remove)
            for k, v in obj.items()
            if k != key_to_remove
        }
    elif isinstance(obj, list):
        return [remove_key(item, key_to_remove) for item in obj]
    else:
        return obj


def filter_by_groups(obj, allowed_groups):
    """
    Filter the collection to keep only items with names in allowed_groups.

    Args:
        obj: The object to filter
        allowed_groups: Set of group names to keep

    Returns:
        Filtered object containing only allowed groups
    """
    if isinstance(obj, dict):
        if "item" in obj and isinstance(obj["item"], list):
            # This is a collection or group with items
            filtered_items = []
            for item in obj["item"]:
                if isinstance(item, dict) and "name" in item:
                    if item["name"] in allowed_groups:
                        # Keep this group as-is (don't filter its sub-items)
                        filtered_items.append(item)
            return {**obj, "item": filtered_items}
        else:
            # Regular dictionary, process recursively
            return {k: filter_by_groups(v, allowed_groups) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [filter_by_groups(item, allowed_groups) for item in obj]
    else:
        return obj


def split_groups_to_files(data, output_dir="./misc/groups"):
    """
    Split the collection into separate files for each group.

    Args:
        data: The processed collection data
        output_dir: Directory to save individual group files
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Extract each group and save to separate files
    if "item" in data:
        for item in data["item"]:
            if "name" in item:
                group_name = item["name"]

                # Create a new collection structure for this group
                group_collection = {
                    "info": {
                        "_postman_id": data["info"]["_postman_id"],
                        "name": f"Transparency Platform Restful API - {group_name}",
                        "description": (
                            f"{group_name} endpoints from the "
                            "Entso-e Transparency Platform Restful API."
                        ),
                        "schema": data["info"]["schema"],
                        "_exporter_id": data["info"]["_exporter_id"],
                        "_collection_link": data["info"]["_collection_link"],
                    },
                    "item": [item],  # Include only this group's items
                }

                # Write to file
                filename = f"{group_name.lower().replace(' ', '_')}.json"
                filepath = os.path.join(output_dir, filename)

                with open(filepath, "w") as f:
                    json.dump(group_collection, f, indent=4)

                print(f"Created: {filepath}")
                print(f"  Group: {group_name}")
                print(f"  Items: {len(item.get('item', []))}")


def main():
    """Main processing function."""
    # Define allowed groups to keep
    allowed_groups = {
        "Market",
        "Load",
        "Generation",
        "Transmission",
        "Outages",
        "Balancing",
        "OMI",
    }

    print("🔧 Processing Entso-e Transparency Platform Postman Collection...")
    print(f"📋 Keeping groups: {', '.join(sorted(allowed_groups))}")
    print()

    # Step 1: Read the original Postman collection
    print("📖 Step 1: Reading original collection...")
    input_file = "./misc/Transparency Platform Restful API.postman_collection.json"
    try:
        with open(input_file, "r") as f:
            data = json.load(f)
        print(f"✅ Loaded: {input_file}")
    except FileNotFoundError:
        print(f"❌ Error: File not found: {input_file}")
        return
    except json.JSONDecodeError as e:
        print(f"❌ Error: Invalid JSON in {input_file}: {e}")
        return

    # Step 2: Remove response fields
    print("\n🧹 Step 2: Removing response fields...")
    cleaned = remove_key(data, "response")

    # Step 3: Filter by allowed groups
    print("\n🔍 Step 3: Filtering by allowed groups...")
    final_data = filter_by_groups(cleaned, allowed_groups)

    # Step 4: Split into individual group files
    print("\n📂 Step 4: Splitting into individual group files...")
    split_groups_to_files(final_data)
    print("✅ All group files created successfully!")


if __name__ == "__main__":
    main()
