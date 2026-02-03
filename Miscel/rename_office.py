import csv

def update_office_parts(input_file, output_file, office_parts_mapping):
    with open(input_file, mode='r', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames  # Get column names
        rows = []

        for row in reader:
            # Update the Office-Part column if the value matches the mapping
            office_part = row['Office-Part']
            if office_part in office_parts_mapping:
                row['Office-Part'] = office_parts_mapping[office_part]
            rows.append(row)

    # Write the updated data to a new file
    with open(output_file, mode='w', encoding='utf-8', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Office-Parts updated and saved to {output_file}.")

# Office-Part mapping
office_parts_mapping = {
    'Al': 'Alleluia',
    'Gr': 'Gradual',
    'Hy': 'Hymn',
    'In': 'Introit',
    'La': 'Lamentation',
    'Ps': 'Psalm',
    'al': 'Alleluia',
    'an': 'Antiphon',
    'ca': 'Canticle',
    'co': 'Communion',
    'gr': 'Gradual',
    'hy': 'Hymn',
    'im': 'Improperia',
    'in': 'Introit',
    'ky': 'Kyriale',
    'of': 'Offertory',
    'or': 'Oratio',
    'ps': 'Psalm',
    'rb': 'Short responsory',
    're': 'Responsory',
    'se': 'Sequence',
    'tr': 'Tract'
}

# Usage
input_csv = 'chant_processed.csv'  # Replace with your input file path
output_csv = 'chant_office_parts_updated.csv'  # Replace with your desired output file path
update_office_parts(input_csv, output_csv, office_parts_mapping)