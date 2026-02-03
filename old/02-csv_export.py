import os
import csv

def extract_gabc_to_csv():
    source_folder = "/Users/martinbaker/Dropbox/04_Music/453_chant-data/chant_to_extract"
    output_file = "/Users/martinbaker/Dropbox/04_Music/453_chant-data/csv-files/chant_extract.csv"
    total_files = 0
    extracted_files = 0
    errors = 0

    # Count total files for progress reporting
    for root, _, files in os.walk(source_folder):
        total_files += sum(1 for file in files if file.endswith(".gabc"))

    print(f"Found {total_files} .gabc files to process...")

    # Open the CSV file for writing
    with open(output_file, "w", encoding="utf-8", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Filename", "Content"])  # Add header row

        processed = 0  # Tracks processed files for progress
        # Iterate through all files in the folder
        for root, _, files in os.walk(source_folder):
            for file in files:
                if file.endswith(".gabc"):
                    processed += 1
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, "r", encoding="utf-8") as gabc_file:
                            content = gabc_file.read().strip()
                            writer.writerow([file, content])
                            extracted_files += 1
                    except Exception as e:
                        print(f"Error reading file {file}: {e}")
                        errors += 1

                    # Report progress
                    if processed % 100 == 0 or processed == total_files:
                        print(f"Processed {processed}/{total_files} files...")

    # Print summary
    print("\n--- Summary ---")
    print(f"Total files found: {total_files}")
    print(f"Files successfully extracted: {extracted_files}")
    print(f"Files with errors: {errors}")
    print(f"Extracted contents saved to: {output_file}")

# Execute the function
if __name__ == "__main__":
    extract_gabc_to_csv()
    '''This is the initial .csv file creation, taking data from every .gabc file in the flat folder created from the original Gregobase export archive'''