import csv
import re

def clean_and_count(input_file, output_file):
    total_ae = 0
    total_æ = 0

    with open(input_file, mode='r', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        rows = []

        for row in reader:
            text_outside_parentheses = row.get('Text Outside Parentheses', '')

            # Count occurrences of 'æ' and 'ae'
            total_æ += text_outside_parentheses.count('æ')
            total_ae += text_outside_parentheses.count('ae')

            # Replace "{ia}" with "ia"
            text_outside_parentheses = text_outside_parentheses.replace("{ia}", "ia")

            # Replace "<sp>'ae</sp>" with "ae"
            text_outside_parentheses = text_outside_parentheses.replace("<sp>'ae</sp>", "ae")

            # Remove "<sp>*</sp>"
            text_outside_parentheses = text_outside_parentheses.replace("<sp>*</sp>", "")

            # Remove all asterisks
            text_outside_parentheses = text_outside_parentheses.replace("*", "")

            # Remove all <sp>...</sp>, <i>...</i>, and <c>...</c> tags and their content
            tags_to_remove = [r"<sp>.*?</sp>", r"<i>.*?</i>", r"<c>.*?</c>"]
            for tag in tags_to_remove:
                text_outside_parentheses = re.sub(tag, "", text_outside_parentheses, flags=re.DOTALL)

            # Patterns to remove
            patterns_to_remove = [
                r"<v>\\greheightstar</v>",
                r"<v>\$\star\$</v>",
                r"E u o u a e\.",
                r"E U O U A E\."
            ]
            for pattern in patterns_to_remove:
                text_outside_parentheses = re.sub(pattern, "", text_outside_parentheses)

            # Remove "E u o u a e"
            text_outside_parentheses = re.sub(r"E u o u a e", "", text_outside_parentheses)

            # Remove anything within {} including the surrounding brackets
            text_outside_parentheses = re.sub(r"\{.*?\}", "", text_outside_parentheses)

            # Replace accented characters
            accented_replacements = {
                'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'ǽ': 'æ'
            }
            for accented_char, replacement in accented_replacements.items():
                text_outside_parentheses = text_outside_parentheses.replace(accented_char, replacement)

            # Replace J with I and j with i
            text_outside_parentheses = text_outside_parentheses.replace('J', 'I').replace('j', 'i')

            # Clean up excessive whitespace
            text_outside_parentheses = re.sub(r'\s+', ' ', text_outside_parentheses).strip()

            # Update the row
            row['Text Outside Parentheses'] = text_outside_parentheses
            rows.append(row)

    # Write the cleaned data to a new file
    with open(output_file, mode='w', encoding='utf-8', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Text Outside Parentheses column cleaned and saved to {output_file}.")
    print(f"Total 'æ': {total_æ}")
    print(f"Total 'ae': {total_ae}")

# Usage
input_csv = 'chant_with_text_outside_parentheses.csv'  # Replace with your input file path
output_csv = 'chant_cleaned_text.csv'  # Replace with your desired output file path
clean_and_count(input_csv, output_csv)