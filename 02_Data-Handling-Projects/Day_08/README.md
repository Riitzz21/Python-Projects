# 🧩 Day 08 - JSON Flattener

## 📌 Project Description

The **JSON Flattener** is a Python utility that converts nested JSON data into a flattened structure.

Nested JSON can contain dictionaries and multiple levels of data, which can sometimes be difficult to analyze or process. This project transforms nested structures into simpler key-value pairs using a dot notation format.

---

## 🚀 Features

* 📄 Reads JSON data from a file
* 🔍 Handles nested dictionaries
* 🔄 Converts nested JSON into a flat structure
* 🗂️ Uses dot notation for nested keys
* 💾 Saves flattened data into an output file
* 📊 Makes complex JSON easier to analyze
* ❌ Handles invalid JSON or file-related errors

---

## 🛠️ Technologies & Concepts Used

* Python
* JSON
* Dictionaries
* Lists
* Recursion
* Functions
* File Handling
* Loops
* Conditional Statements
* Exception Handling
* Data Transformation

---

## 🔄 How It Works

```text
Nested JSON
     ↓
Read JSON Data
     ↓
Identify Nested Structures
     ↓
Recursively Process Data
     ↓
Create Flattened Keys
     ↓
Generate Flat JSON
```

---

## 📊 Example

### Input JSON

```json
{
    "student": {
        "name": "Rajeshwari",
        "details": {
            "course": "MCA",
            "year": 2026
        }
    }
}
```

### Flattened JSON

```json
{
    "student.name": "Rajeshwari",
    "student.details.course": "MCA",
    "student.details.year": 2026
}
```

The nested keys are combined using `.` notation.

---

## 📚 What I Learned

* How nested JSON structures work.
* How to access values inside nested dictionaries.
* How recursion can be used to process nested data.
* How to transform complex data into a simpler structure.
* How to read and write JSON files using Python.
* How data transformation can make information easier to analyze.
* How to handle nested data programmatically.

---

## 🎯 Learning Outcome

This project helped me understand how to process and transform nested JSON data into a flat structure.

It also strengthened my understanding of dictionaries, recursion, JSON processing, and data transformation.

---

## 📂 Project Structure

```text
Day_08/
│
├── 08_Day_08.py
├── input.json
├── output.json
└── README.md
```

---

Part of my **10-Day Data Handling Python Projects Challenge** 📊🐍✨
