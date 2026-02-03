import os

def correct_file_format(folder_path):
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        # Process only files
        if os.path.isfile(file_path):
            print(f"Processing: {file_name}")  # Debugging message

            # Check if ".gabc" exists in the name
            if ".gabc" in file_name:
                # Split the file name at ".gabc"
                name, suffix = file_name.split(".gabc", 1)
                suffix = suffix.strip()  # Remove any extra spaces around the suffix

                # Split the base name into parts
                parts = name.split("-")

                # Print for debugging
                print(f"Base name: {name}")
                print(f"Suffix: {suffix}")
                print(f"Parts: {parts}")

                # Ensure there are enough parts to rearrange
                if len(parts) >= 3:  # At least [type], [some_words], [year/numbers]
                    # Reassemble the new file name
                    new_name = f"{'-'.join(parts[:-2])}-{parts[-2]}-{parts[-1]}.gabc"
                    if suffix:  # Add the suffix back if it exists
                        new_name += suffix

                    # Rename the file
                    new_file_path = os.path.join(folder_path, new_name)
                    os.rename(file_path, new_file_path)
                    print(f"Renamed: {file_name} -> {new_name}")
                else:
                    print(f"Skipping: {file_name} (unexpected format)")
            else:
                print(f"Skipping: {file_name} (no .gabc in name)")

if __name__ == "__main__":
    folder_path = "graduale_romanum-complete"  # Update this to your folder's path
    correct_file_format(folder_path)