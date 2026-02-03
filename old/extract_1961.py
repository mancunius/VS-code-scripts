import os
import shutil

def flatten_and_rename_files(source_root, target_folder, prefix_year):
    # Ensure the target folder exists
    os.makedirs(target_folder, exist_ok=True)

    # Traverse each subfolder in the source directory
    for subfolder in os.listdir(source_root):
        subfolder_path = os.path.join(source_root, subfolder)

        # Ensure we are processing a directory
        if os.path.isdir(subfolder_path):
            for file_name in os.listdir(subfolder_path):
                file_path = os.path.join(subfolder_path, file_name)

                # Ensure we are processing a file
                if os.path.isfile(file_path):
                    # Create the new name based on the subfolder and original file name
                    new_name = f"{prefix_year}-{subfolder}-{file_name}"
                    target_path = os.path.join(target_folder, new_name)

                    # Copy and rename the file to the target folder
                    shutil.copy(file_path, target_path)
                    print(f"Copied and renamed: {file_path} -> {target_path}")

if __name__ == "__main__":
    # Source folder and year prefix
    source_root = "1961_graduale_romanum"  # Replace with your source folder path
    target_folder = "graduale_romanum_b"  # Replace with your target folder path
    prefix_year = "1961"

    # Flatten and rename files
    flatten_and_rename_files(source_root, target_folder, prefix_year)