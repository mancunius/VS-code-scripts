import csv
import re

def process_csv(input_file, output_file):
    with open(input_file, mode='r', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        fieldnames = ['Filename', 'Name', 'Office-Part', 'Mode', 'Book', 'Occasion', 'Content', 'Removed']
        rows = []

        for row in reader:
            # Use the correct column names
            content = row['Content']
            filename = row['Filename']
            removed_text = []

            # Extract and remove the "name" field, limit to 70 characters
            name_match = re.search(r"name:\s*([^{}]+?)(?=office-part:|mode:|book:|occasion:|transcriber:|$)", content)
            if name_match:
                removed_text.append(f"name: {name_match.group(1).strip()}")
            name = name_match.group(1).strip()[:70] if name_match else ""  # Limit to 70 characters
            content = re.sub(r"name:\s*([^{}]+?)(?=office-part:|mode:|book:|occasion:|transcriber:|$)", "", content)

            # Extract and remove the "office-part" field (only two letters after "office-part:")
            office_part_match = re.search(r"office-part:\s*([a-zA-Z]{2})", content)
            if office_part_match:
                removed_text.append(f"office-part: {office_part_match.group(1).strip()}")
            office_part = office_part_match.group(1).strip() if office_part_match else ""
            content = re.sub(r"office-part:\s*[a-zA-Z]{2}", "", content)

            # Extract and remove the "mode" field
            mode_match = re.search(r"mode:\s*(\w+)", content)
            if mode_match:
                removed_text.append(f"mode: {mode_match.group(1).strip()}")
            mode = mode_match.group(1).strip() if mode_match else ""
            content = re.sub(r"mode:\s*\w+", "", content)

            # Extract and remove the "book" field, limiting to 50 characters
            book_match = re.search(r"book:\s*([^{}]+?)(?=office-part:|mode:|occasion:|transcriber:|$)", content)
            if book_match:
                removed_text.append(f"book: {book_match.group(1).strip()}")
            book = book_match.group(1).strip()[:50] if book_match else ""
            content = re.sub(r"book:\s*([^{}]+?)(?=office-part:|mode:|occasion:|transcriber:|$)", "", content)

            # Extract and remove the "occasion" field, limiting to 50 characters
            occasion_match = re.search(r"occasion:\s*([^{}]+?)(?=office-part:|mode:|book:|transcriber:|$)", content)
            if occasion_match:
                removed_text.append(f"occasion: {occasion_match.group(1).strip()}")
            occasion = occasion_match.group(1).strip()[:50] if occasion_match else ""
            content = re.sub(r"occasion:\s*([^{}]+?)(?=office-part:|mode:|book:|transcriber:|$)", "", content)

            # Remove all characters before the first (c or (f
            content_match = re.search(r"\(cb?\d\)(.|\n)*|\(fb?\d\)(.|\n)*are", content)
            if content_match:
                removed_text.append(content[:content_match.start()].strip())
            content = content_match.group(0).strip() if content_match else content

            # Clean up excessive whitespace
            content = re.sub(r"\s+", " ", content).strip()

            # Combine removed text into a single string
            removed_text_combined = " | ".join(removed_text)

            # Append the processed row
            rows.append({
                'Filename': filename,
                'Name': name,
                'Office-Part': office_part,
                'Mode': mode,
                'Book': book,
                'Occasion': occasion,
                'Content': content,
                'Removed': removed_text_combined
            })

    # Write the new CSV file
    with open(output_file, mode='w', encoding='utf-8', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    # Summary
    print(f"Processed {len(rows)} rows. Output saved to {output_file}.")

# Usage
input_csv = '/Users/martinbaker/Dropbox/04_Music/453_chant-data/csv-files/chant_extract.csv'  # Replace with your input file path
output_csv = '/Users/martinbaker/Dropbox/04_Music/453_chant-data/csv-files/chant_processed.csv'  # Replace with your desired output file path
process_csv(input_csv, output_csv)