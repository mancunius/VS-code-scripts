import os
import shutil

def extract_and_flatten_gabc_files():
    source_folder = "/Users/martinbaker/Dropbox/04_Music/453_chant-data/gabc_export"
    destination_folder = "/Users/martinbaker/Dropbox/04_Music/453_chant-data/chant_to_extract"

    # Ensure the destination folder exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Counters for statistics
    extracted_count = 0
    renamed_count = 0

    # Process the source folder recursively
    for root, _, files in os.walk(source_folder):
        for file in files:
            if file.endswith(".gabc"):
                extracted_count += 1
                
                # Determine the source file path
                source_path = os.path.join(root, file)
                
                # Determine the destination file path
                base_name, ext = os.path.splitext(file)
                destination_path = os.path.join(destination_folder, file)
                
                # Handle name conflicts
                suffix = 1
                while os.path.exists(destination_path):
                    destination_path = os.path.join(
                        destination_folder, f"{base_name}_{suffix}{ext}"
                    )
                    suffix += 1
                
                if suffix > 1:
                    renamed_count += 1
                
                # Copy the file to the destination folder
                shutil.copy2(source_path, destination_path)

    # Report results
    print(f"Total files extracted: {extracted_count}")
    print(f"Files renamed due to conflicts: {renamed_count}")

# Execute the function
if __name__ == "__main__":
    extract_and_flatten_gabc_files()
    
''' please write a python3 script to do as follows:

there is a folder called gabc_export which contains multiple files in multiple subfolders. Each file has the suffix .gabc

Pull all of the .gabc files from all of the subfolders and place them in the folder chant_to_extract which is in the same directory as the gabc_export folder. Make the sturcture flat so there are no subfolders in the gabc_export folder

If there are any files with identical names add an integer at the end of the filename and before the .gabc suffix so that they can co-exist.

End by reporting the number of files extracted and the number of renamed files.

The script will be run from the same directory as these folders.'''