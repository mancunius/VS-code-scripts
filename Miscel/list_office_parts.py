import csv

def get_unique_office_parts(file_path):
    unique_office_parts = set()  # Use a set to store unique values

    with open(file_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            office_part = row['Office-part-updated']
            if office_part:  # Ensure the value is not empty
                unique_office_parts.add(office_part)

    return unique_office_parts

# Usage
file_path = '/Users/martinbaker/Dropbox/04_Music/453_chant-data/csv-files/chant_tidy_flats.csv'  # Replace with your file path
unique_office_parts = get_unique_office_parts(file_path)
print(f"Unique Office-Part-updated values ({len(unique_office_parts)}):")
print(sorted(unique_office_parts))
'''This is the function that will extract the unique office parts from the processed .csv file created in the previous step'''
# This function reads the processed CSV file and extracts unique values from the 'Office-Part' column. It uses a set to store unique values and returns the set after processing all rows. The function can be used to extract unique office parts from the processed CSV file.
# The `get_unique_office_parts` function takes a file path as input and returns a set of unique office parts extracted from the 'Office-Part' column in the CSV file. The function reads the CSV file using the `csv.DictReader` class and iterates over each row to extract the 'Office-Part' value. It adds non-empty values to the set to ensure only unique values are stored.
# The function is used to extract unique office parts from the 'chant_processed.csv' file, and the results are printed to the console. The unique office parts are sorted for better readability. The function can be adapted to extract unique values from other columns by changing the column name in the code.
# The output of this script is a list of unique office parts extracted from the processed CSV file. The unique values are sorted alphabetically for better readability. This script provides a way to identify the different office parts present in the processed data and can be used to analyze the distribution of office parts in the dataset.
# The script can be further extended to perform additional analysis on the extracted office parts, such as counting the frequency of each office part or visualizing the distribution of office parts in the dataset. This information can provide insights into the composition of the dataset and help in understanding the structure of the processed data.