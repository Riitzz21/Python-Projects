"""
Challenge : JSON-Excel Converter tool

Create a python utility that reads structured data (like you'd
 get from an API) from a `.json` file and converts it to a 
 CSV file that can be opened an excel.

 Your program should :
 1. Read from a file named `api_data.json` in the same folder.
 2. Convert the JSON content (a list of dictionaries) into `converted_data.csv`.
 3. Automatically extract field names as CSV headers.
 4. Handle nested structures by flattening or skipping them.

 Bonus :
 - Provide feedback on how many records were converted.
 - Allow user to define which fields to extract.
 - Handle missing fields gracefully
"""

import json
import csv
import os

INPUT_FILE = "Data-Handling-Projects/Day_06/api_data.json"
OUTPUT_FILE = "converted_data.csv"

def load_json_data(filename):
    if not os.path.exists(filename):
        print("JSON file not found!")
        return []

    with open(filename, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except:
            print("Invalid JSON format!")

def convert_to_csv(data, output_file):
    if not data:
        print("No data to convert!")
        return
    
    field_name = list(data[0].keys())

    with open(output_file, "w", newline="", encoding="utf-8") as f:

        writer = csv.DictWriter(f, fieldnames=field_name)
        writer.writeheader()

        for record in data:
            writer.writerow(record)

    print(f"Converted {len(data)} records to {output_file}")

def main():
    print("Converting JSON to CSV...")
    data = load_json_data(INPUT_FILE)
    convert_to_csv(data, OUTPUT_FILE)


if __name__ == "__main__":
    main()

