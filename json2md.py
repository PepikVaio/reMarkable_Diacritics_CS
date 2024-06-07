import pandas as pd
import os
import sys

def main(input_file, output_file):
    """Convert a JSON file to a Markdown table.

    Args:
        input_file (str): The path to the input JSON file.
        output_file (str): The path to the output Markdown table file.

    Returns:
        None
    """
    # Read the JSON file into a Pandas DataFrame
    df = pd.read_json(input_file, orient='records')

    # Convert the DataFrame to a Markdown table
    md_table = df.to_markdown()

    # Write the Markdown table to a file
    with open(output_file, 'w') as f:
        f.write(md_table)

    # Print the full path to the input and output files
    print("Input file: ", os.path.abspath(input_file))
    print("Output file:", os.path.abspath(output_file))

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python json2md.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    main(input_file, output_file)
