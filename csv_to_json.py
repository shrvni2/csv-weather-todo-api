```python
import csv
import json
import argparse
import os

def csv_to_json(csv_file_path, json_file_path):
    """
    Converts a CSV file to a JSON file.
    
    Args:
        csv_file_path (str): The path to the CSV file.
        json_file_path (str): The path to the JSON file.
    """
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = [row for row in csv_reader]

    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def main():
    parser = argparse.ArgumentParser(description='CSV to JSON converter')
    parser.add_argument('-c', '--csv', help='Path to the CSV file', required=True)
    parser.add_argument('-j', '--json', help='Path to the JSON file', required=True)
    args = parser.parse_args()

    csv_file_path = args.csv
    json_file_path = args.json

    if not os.path.exists(csv_file_path):
        print(f"Error: The CSV file '{csv_file_path}' does not exist.")
        return

    if os.path.exists(json_file_path):
        overwrite = input(f"The JSON file '{json_file_path}' already exists. Do you want to overwrite it? (y/n): ")
        if overwrite.lower() != 'y':
            print("Conversion cancelled.")
            return

    csv_to_json(csv_file_path, json_file_path)
    print(f"Successfully converted '{csv_file_path}' to '{json_file_path}'.")

if __name__ == '__main__':
    main()
```