def flatten_to_records(data, parent_key="", sep="."):
    """
    Recursively flattens JSON into a list of records (dicts) suitable for pandas.
    Lists of dicts are expanded into multiple rows.
    """
    if isinstance(data, dict):
        items = {}
        for k, v in data.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.update(flatten_to_records(v, new_key, sep=sep)[0])  # merge dict
            elif isinstance(v, list):
                # Expand list elements into multiple records
                list_records = []
                for elem in v:
                    if isinstance(elem, dict):
                        sub_records = flatten_to_records(elem, new_key, sep=sep)
                        list_records.extend(sub_records)
                    else:
                        list_records.append({new_key: elem})
                # Cross join if multiple records, else just keep one
                if list_records:
                    return [dict(items, **lr) for lr in list_records]
            else:
                items[new_key] = v
        return [items]
    elif isinstance(data, list):
        records = []
        for elem in data:
            records.extend(flatten_to_records(elem, parent_key, sep=sep))
        return records
    else:
        return [{parent_key: data}]


def json_to_dataframe(data, sep="."):
    """
    Converts a nested JSON/dict/list into a pandas DataFrame.
    """
    records = flatten_to_records(data, sep=sep)
    return pd.DataFrame(records)
