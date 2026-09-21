"""
Challenge : JSON Flattener

{
  "user" : {
      "id" : 1,
      "name" : Ritzz
      "email" : ritzz@gmail.com,
      "address" : {
         "city" : "Indore",
         "pincode" : 453001
      }
  },
  "Roles" : ["Admin", "Editor"],
  "is_active" : true 
}

Flatten this to  :

{
  "user.id" : 1,
  "user.name" : Ritzz,
  "user.email" : ritzz@gmail.com,
  "user.address.pincode" : 453001,
  "Roles.0" : "Admin",
  "Roles.1" : "Editor",
  "is_active" : true
}

"""

import json
import os

INPUT_FILE = "Data-Handling-Projects/Day_08/nested_data.json"
OUTPUT_FILE = "flatten_data.json"

def flatten_json(data, parent_key='', sep='.'):
    items = {}

    if isinstance(data, dict):
        for k, v in data.items():
            full_key = f"{parent_key}{sep}{k}" if parent_key else k
            print(full_key)
            items.update(flatten_json(v, full_key, sep=sep))


    elif isinstance(data, list):
        for idx, item in enumerate(data):
            full_key = f"{parent_key}{sep}{idx}" if parent_key else str(idx)
            items.update(flatten_json(item, full_key, sep=sep))

    else:
        items[parent_key] = data

    return items

def main():
    if not os.path.exists(INPUT_FILE):
        print("No input file found!")
        return

    try:
        with open(INPUT_FILE, 'r', encoding="utf-8") as f:
            data = json.load(f)

        sep = input("Enter your seperator like . or -: ").strip() or '.'

        flattened = flatten_json(data, sep=sep)

        with open(OUTPUT_FILE, 'w', encoding="utf-8") as f:
            json.dump(flattened, f, indent=2)

            print(f"Flattened JSON data saved to {OUTPUT_FILE}")

    except Exception as e:
        print("Failed to flattened data", e)

if __name__ == "__main__":
    main()