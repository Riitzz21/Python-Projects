"""
Challenge : CSV-To-JSON Converter tool

Create a python utility that reads structured data (like you'd get from an API)
from a `.json` file and converts it into a CSV file that can be opened
in Excel.

Your program should :
1. Read from a file named `api_data.json` in the same folder.
2. Convert the JSON content (a list of dictionaries) into `converted_data.csv`.
3. Automatically extract field names as CSV headers.
4. Handle nested structures by flattening or skipping them.

Bonus :
- Provide feedback on how many records were converted.
- Allow user to define which fields to extract.
- Handle missing fields gracefully.

"""

import os
import json
import csv

INPUT_FILE = "Data-Handling-Projects/Day_07/raw_data.csv"
OUTPUT_FILE = "converted_data.json"

def load_cv_data(filename):
    if not os.path.exists(filename):
        print("CSV file not found!")
        return []

    with open(filename, 'r', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        data = list(reader)
        print(data)
        return data

def sava_as_json(data, filename):
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"✅Converted {len(data)} records to {filename}")

def preview_data(data, count=3):
    for row in data[:count]:
        print(json.dumps(row, indent=2))
    print("......")

def main():
    data = load_cv_data(INPUT_FILE)
    if not data:
        return
    sava_as_json(data, OUTPUT_FILE)
    preview_data(data)

if __name__ == "__main__":
    main() 
    
