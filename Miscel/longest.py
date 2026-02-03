import csv

def find_longest_in_columns(input_file, output_file):
    with open(input_file, mode='r', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        column_max = {column: "" for column in reader.fieldnames}

        for row in reader:
            for column, value in row.items():
                # Update the longest string for each column
                if len(value.strip()) > len(column_max[column]):
                    column_max[column] = value.strip()

    # Prepare the output CSV
    with open(output_file, mode='w', encoding='utf-8', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['Column', 'Longest String'])  # Header
        for column, longest_string in column_max.items():
            writer.writerow([column, longest_string])

    # Summary
    print(f"Longest strings for each column saved to {output_file}.")

# Usage
input_csv = '/Users/martinbaker/Dropbox/04_Music/453_chant-data/csv-files/chant_tidy_flats.csv'  # Input file path
output_csv = '/Users/martinbaker/Dropbox/04_Music/453_chant-data/csv-files/longest_strings.csv'  # Output file path
find_longest_in_columns(input_csv, output_csv) 