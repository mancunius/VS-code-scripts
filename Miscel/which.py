import csv

def list_files_by_office_parts(file_path, office_parts_to_match):
    matching_files = []  # List to store filenames that match the criteria

    with open(file_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            office_part = row['Office-part']
            filename = row['Filename']
            if office_part in office_parts_to_match:
                matching_files.append(filename)

    return matching_files

# Usage
file_path = '/Users/martinbaker/Dropbox/04_Music/453_chant-data/csv-files/chant_processed.csv'  # Replace with your file path
office_parts_to_match = {'Ad', 'Ve', 'pa', 'pr', 'rb', 'rh', 'su', 'tp', 'va'}  # Values to match
matching_files = list_files_by_office_parts(file_path, office_parts_to_match)

# Output
print(f"Found {len(matching_files)} matching files:")
for file in matching_files:
    print(file)