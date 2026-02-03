import os

def rename_files(folder_path):
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        # Process only files
        if os.path.isfile(file_path):
            # Check if the file has the ".gabc" extension
            if file_name.endswith(".gabc"):
                # Try to extract and reorder the filename components
                try:
                    # Split the filename based on the hyphen separator
                    year, type_, rest = file_name.split("-", 2)
                    
                    # Split the rest into numbers and the actual content
                    numbers, some_words = rest.split("_", 1)
                    
                    # Replace spaces with underscores in `some_words`
                    some_words = some_words.replace(" ", "_")
                    
                    # Reassemble the filename in the required format
                    new_name = f"{type_}-{some_words}-{year}-{numbers}.gabc"
                    new_file_path = os.path.join(folder_path, new_name)
                    
                    # Rename the file
                    os.rename(file_path, new_file_path)
                    print(f"Renamed: {file_name} -> {new_name}")
                except ValueError:
                    # If the filename doesn't match the expected format, skip it
                    print(f"Skipping: {file_name} (unexpected format)")

if __name__ == "__main__":
    folder_path = "graduale_romanum-complete"  # Update with your folder path
    rename_files(folder_path)