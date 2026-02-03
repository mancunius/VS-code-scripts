import csv
import re

def process_csv(input_file, output_file):
    # Define the fields to extract
    fields_to_extract = [
        'annotation', 'author', 'book', 'centering-scheme', 'commentary',
        'font', 'fontsize', 'height', 'initial-style', 'libitum', 
        'nabc-lines', 'name', 'occasion', 'office-part', 'text-right',
        'transcriber', 'user-notes', 'mode'
    ]
    
    # Define fieldnames for output CSV (including Folder)
    fieldnames = ['Filename', 'Folder'] + [field.capitalize() for field in fields_to_extract] + ['Content', 'Removed']
    
    rows = []
    
    with open(input_file, mode='r', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        
        for row in reader:
            content = row['Content']
            filename = row['Filename']
            folder = row['Folder']  # Retain the Folder column
            removed_text = []
            
            # Initialize dictionary for extracted data
            extracted_data = {field.capitalize(): '' for field in fields_to_extract}
            
            # Extract each field based on a regex
            for field in fields_to_extract:
                # Adjust the regex to handle fields followed by ;, %% or end of line
                if field == 'mode':
                    # For mode, capture 1-2 letters or a digit followed by either `;`, `%%` or end of line
                    regex = fr"{field}:\s*([a-zA-Z0-9]+)(?=\s*(;|%%|\n|$))"
                else:
                    # Default regex for other fields
                    regex = fr"{field}:\s*([^;%%\n]+?)(?=\s*(;|%%|\n|$))"
                
                # Search for the field in the content
                match = re.search(regex, content)
                if match:
                    extracted_value = match.group(1).strip()  # Strip leading/trailing spaces
                    extracted_data[field.capitalize()] = extracted_value
                    removed_text.append(f"{field}: {extracted_value}")
                    # Remove the matched field from content
                    content = re.sub(regex, '', content)

            # After extracting fields, any leftover text is stored in 'Removed'
            removed_text_combined = " | ".join(removed_text)
            
            # Append processed row to the list
            rows.append({
                'Filename': filename.strip(),
                'Folder': folder.strip(),  # Retain Folder value
                **extracted_data,
                'Content': content.strip(),
                'Removed': removed_text_combined.strip()
            })
    
    # Write output CSV
    with open(output_file, mode='w', encoding='utf-8', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    # Summary
    print(f"Processed {len(rows)} rows. Output saved to {output_file}.")

# Usage
input_csv = '/Users/martinbaker/Dropbox/04_Music/453_chant-data/csv-files/chant_folder_extract.csv'  # Replace with your input file path
output_csv = '/Users/martinbaker/Dropbox/04_Music/453_chant-data/csv-files/chant_processed.csv'  # Replace with your desired output file path
process_csv(input_csv, output_csv)
''' The first extraction process from the .gabc files has been completed, and the data has been saved to a .csv file. The next step is to process this data to extract specific fields and save the results to a new CSV file. This script reads the initial CSV file, extracts specific fields from the 'Content' column using regular expressions, and writes the extracted data to a new CSV file. The fields to extract are defined in the `fields_to_extract` list, and the regular expressions are customized for each field. The script also removes the extracted fields from the 'Content' column and stores the removed text in the 'Removed' column. The output CSV file contains the extracted fields, the original content, and the removed text for each row. The script provides a summary of the processing results, including the number of rows processed and the output file path. Veronica helped with the regex codes.'''