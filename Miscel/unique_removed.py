import csv
import re

def extract_unique_words_with_colon(input_file):
    unique_words = set()  # Use a set to store unique values

    with open(input_file, mode='r', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        
        for row in reader:
            # Get the 'Removed' column content
            removed_content = row.get('Removed', '')
            
            # Find all patterns followed by a colon, excluding words with parentheses
            matches = re.findall(r'\b(?!\S*\(.*?\))([^\s:]+):', removed_content)  
            unique_words.update(matches)  # Add matches to the set
    
    # Output the unique words
    print("Unique words followed by a colon (excluding those with parentheses):")
    for word in sorted(unique_words):
        print(word)
    
    print(f"\nTotal unique words: {len(unique_words)}")

# Usage
input_csv = '/Users/martinbaker/Dropbox/04_Music/453_chant-data/csv-files/chant_processed.csv'  # Replace with your file path
extract_unique_words_with_colon(input_csv)