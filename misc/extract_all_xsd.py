import os
import shutil
import tempfile

import py7zr

# Configuration
archive_path = "xsd_schema.7z"  # The file you downloaded in step 1
output_folder = "xsd"

# 1. Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

print(f"Opening {archive_path}...")

# 2. Extract the 7z archive to a temporary directory, then flatten it into output_folder
with tempfile.TemporaryDirectory() as tmp_dir:
    with py7zr.SevenZipFile(archive_path, mode="r") as archive:
        archive.extractall(path=tmp_dir)

    for root, _, files in os.walk(tmp_dir):
        for filename in files:
            source_path = os.path.join(root, filename)
            target_path = os.path.join(output_folder, filename)

            shutil.copyfile(source_path, target_path)

            print(f"Extracted: {filename}")

print("All files extracted successfully!")
