import os
import csv

def extract_gabc_contents(input_directory, output_csv):
    # List to store extracted data
    rows = []

    # Traverse the directory and process files
    for root, _, files in os.walk(input_directory):
        for file in files:
            if file.endswith('.gabc'):
                # Get the folder immediately under "gabc_export"
                relative_path = os.path.relpath(root, input_directory)
                folder = relative_path.split(os.sep)[0]

                # Get the full path of the file and read its content
                file_path = os.path.join(root, file)
                with open(file_path, mode='r', encoding='utf-8') as f:
                    content = f.read()

                # Append the data as a row
                rows.append({
                    'Filename': file,
                    'Folder': folder,
                    'Content': content
                })

    # Write the data to a CSV file
    with open(output_csv, mode='w', encoding='utf-8', newline='') as csv_file:
        fieldnames = ['Filename', 'Folder', 'Content']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(rows)

    print(f"Extraction complete. Data saved to {output_csv}")

# Paths
input_directory = "/Users/martinbaker/Dropbox/04_Music/453_chant-data/gabc_export"  # Adjust as needed
output_csv = "/Users/martinbaker/Dropbox/04_Music/453_chant-data/csv-files/chant_folder_extract.csv"  # Adjust as needed

# Run the function
extract_gabc_contents(input_directory, output_csv)