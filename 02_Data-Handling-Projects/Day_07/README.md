# 🔄 Day 07 - CSV-to-JSON Converter Tool

## 📌 Project Description

The **CSV-to-JSON Converter Tool** is a Python utility that converts structured data from a CSV file into JSON format.

The project reads tabular data from a CSV file, processes each row, and converts the records into a structured JSON format. This makes the data easier to use with applications, APIs, and other systems that work with JSON.

---

## 🚀 Features

* 📄 Reads data from CSV files
* 🔄 Converts CSV records into JSON format
* 💾 Saves converted data into a JSON file
* 📊 Handles structured tabular data
* 🗂️ Preserves CSV column names as JSON keys
* ❌ Handles file and data-related errors
* 🖥️ Simple command-line interface

---

## 🛠️ Technologies & Concepts Used

* Python
* CSV File Handling
* JSON
* File Handling
* Lists
* Dictionaries
* Loops
* Functions
* `csv.DictReader`
* `json.dump()`
* Exception Handling

---

## 🔄 How It Works

```text
CSV File
   ↓
Read CSV Data
   ↓
Convert Each Row into a Dictionary
   ↓
Store Records in a List
   ↓
Convert List into JSON
   ↓
Save JSON File
```

---

## 📊 Example

### Input CSV

```csv
Name,Age,City
Rajeshwari,21,Indore
Aman,22,Bhopal
Neha,21,Delhi
```

### Output JSON

```json
[
    {
        "Name": "Rajeshwari",
        "Age": "21",
        "City": "Indore"
    },
    {
        "Name": "Aman",
        "Age": "22",
        "City": "Bhopal"
    },
    {
        "Name": "Neha",
        "Age": "21",
        "City": "Delhi"
    }
]
```

---

## 📚 What I Learned

* How to read CSV files using Python.
* How to use `csv.DictReader`.
* How CSV rows can be represented as dictionaries.
* How to work with lists of dictionaries.
* How to create JSON data using Python.
* How to write structured data to a JSON file.
* How to convert data between different formats.
* How to handle file-related errors.

---

## 🎯 Learning Outcome

This project helped me understand how Python can transform tabular CSV data into structured JSON data.

It also improved my understanding of dictionaries, lists, file handling, and data serialization.

---

## 📂 Project Structure

```text
Day_07/
│
├── 07_Day_07.py
├── input.csv
├── output.json
└── README.md
```

---

Part of my **10-Day Data Handling Python Projects Challenge** 📊🐍✨
