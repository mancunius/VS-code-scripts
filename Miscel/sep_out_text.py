import csv
import re

def add_text_outside_parentheses(input_file, output_file):
    with open(input_file, mode='r', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames + ['Text Outside Parentheses']  # Add a new column name
        rows = []

        for row in reader:
            content = row['Content']
            
            # Extract text outside parentheses
            text_outside_parentheses = re.sub(r'\([^)]*\)', '', content).strip()
            
            # Add the new column value to the row
            row['Text Outside Parentheses'] = text_outside_parentheses
            rows.append(row)

    # Write the updated data to a new file
    with open(output_file, mode='w', encoding='utf-8', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Text outside parentheses added as a new column and saved to {output_file}.")

# Usage
input_csv = 'chant_office_parts_updated.csv'  # Replace with your input file path
output_csv = 'chant_with_text_outside_parentheses.csv'  # Replace with your desired output file path
add_text_outside_parentheses(input_csv, output_csv)