import pandas as pd
import os
import sys
import json

def main(input_file, output_file):
    """Convert a ODS file to a JSON file.

    Args:
        input_file (str): The path to the input ODS file.
        output_file (str): The path to the output JSON file.

    Returns:
        None
    """
    # Read the ODS file into a Pandas DataFrame
    df = pd.read_excel(input_file)

    # Convert the DataFrame to a ODS file
    csv_file = 'file.csv'
    df.to_csv(csv_file, index=False, encoding='utf-8')

    # Read the ODS file into a Pandas DataFrame
    fixed_lines = []
    line_number = 0
    with open(csv_file, 'r', encoding='utf-8') as f:
        for line in f:
            line_number += 1
            fixed_line = ''
            for char in line:
                try:
                    fixed_line += char
                except Exception as e:
                    print("Line {}: Invalid character '{}' stripped".format(line_number, char))
            fixed_lines.append(fixed_line)

    # Write the cleaned lines to a file
    cleaned_file = 'cleaned.csv'
    with open(cleaned_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(fixed_lines))

    # Read the cleaned ODS file into a Pandas DataFrame
    df = pd.read_csv(cleaned_file, encoding='utf-8')

    # Convert the DataFrame to a JSON object
    json_obj = df.to_json(orient='records', force_ascii=False)

    # Write the JSON object to a file
    with open(output_file, 'w') as f:
        f.write(json.dumps(json.loads(json_obj), ensure_ascii=False, indent=4))


    # Print the full path to the input and output files
    print("Input file: ", os.path.abspath(input_file))
    print("Output file:", os.path.abspath(output_file))

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python ods2json.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    main(input_file, output_file)
