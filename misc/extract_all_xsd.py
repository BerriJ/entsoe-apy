import os
import shutil
import zipfile

# Configuration
zip_file_path = "xsd_schema.zip"  # The file you downloaded in step 1
output_folder = "xsd"

# 1. Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

print(f"Opening {zip_file_path}...")

# 2. Open the ZIP file
with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
    # Loop through every item inside the zip
    for member in zip_ref.infolist():
        # Skip directories, we only want files
        if member.is_dir():
            continue

        # 3. Get the filename only (stripping away the folder path)
        # e.g., "nested/folder/report.pdf" becomes just "report.pdf"
        filename = os.path.basename(member.filename)

        # Skip system files or empty names if any exist
        if not filename:
            continue

        # 4. Define the final path (flattened)
        target_path = os.path.join(output_folder, filename)

        # 5. Extract the file content and write it to the new location
        # We use shutil.copyfileobj for efficiency with large files
        with zip_ref.open(member) as source, open(target_path, "wb") as target:
            shutil.copyfileobj(source, target)

        print(f"Extracted: {filename}")

print("All files extracted successfully!")
