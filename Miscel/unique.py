import csv
from collections import Counter

def get_sorted_values(input_file, column_name):
    values = []
    
    with open(input_file, mode='r', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        
        for row in reader:
            value = row[column_name].strip()  # Strip any leading/trailing spaces
            if value:
                values.append(value)
    
    # Count occurrences of each value and sort by frequency
    value_counts = Counter(values)
    sorted_values = value_counts.most_common()  # Sort by frequency (most common first)
    
    return sorted_values

# Usage
input_csv = '/Users/martinbaker/Dropbox/04_Music/453_chant-data/csv-files/chant_tidy_flats.csv'
column_name = 'Clefs'  # Specify the column name you're interested in

sorted_books = get_sorted_values(input_csv, column_name)

# Output sorted values by frequency
print(f"Most popular values in the '{column_name}' column:")
for book, count in sorted_books:
    print(f"{book}: {count}")