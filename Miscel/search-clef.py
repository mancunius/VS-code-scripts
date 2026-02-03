import csv

def save_empty_clef_rows(input_file, output_file):
    with open(input_file, mode='r', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        
        # Fieldnames for output file
        fieldnames = ['Name', 'Content']
        
        # Collect rows where Clefs column is empty
        rows_to_save = [
            {'Name': row.get('Name', 'Unnamed'), 'Content': row.get('Content', '')}
            for row in reader if not row['Clefs'].strip()
        ]
    
    # Write rows to the output file
    with open(output_file, mode='w', encoding='utf-8', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows_to_save)

    print(f"Saved {len(rows_to_save)} rows with empty Clefs to {output_file}.")

# File paths
input_csv = '/Users/martinbaker/Dropbox/04_Music/453_chant-data/csv-files/chant_tidy_flats.csv'
output_csv = '/Users/martinbaker/Dropbox/04_Music/453_chant-data/csv-files/chant_empty_clefs.csv'

# Run the function
save_empty_clef_rows(input_csv, output_csv)