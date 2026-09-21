# 🔄 Day 06 - JSON–Excel Converter Tool

## 📌 Project Description

The **JSON–Excel Converter Tool** is a Python utility that allows users to convert structured data between JSON and Excel formats.

The project demonstrates how Python can read structured JSON data, convert it into tabular Excel data, and also convert Excel data back into JSON format.

---

## 🚀 Features

* 📄 Convert JSON files to Excel
* 📊 Convert Excel files to JSON
* 🔄 Supports two-way data conversion
* 💾 Creates converted output files
* 🗂️ Handles structured data
* 🖥️ Simple command-line interface
* ❌ Handles invalid file or data input

---

## 🛠️ Technologies & Concepts Used

* Python
* JSON
* Excel
* File Handling
* Dictionaries
* Lists
* Pandas
* DataFrames
* `json.load()`
* `json.dump()`
* `pandas.read_json()`
* `pandas.read_excel()`
* `DataFrame.to_excel()`
* `DataFrame.to_json()`
* Exception Handling

---

## 🔄 How It Works

```text
             User selects conversion
                       ↓
              ┌────────┴────────┐
              ↓                 ↓
          JSON → Excel      Excel → JSON
              ↓                 ↓
        Read JSON data     Read Excel data
              ↓                 ↓
        Create DataFrame   Create DataFrame
              ↓                 ↓
        Save Excel file    Save JSON file
```

---

## 📊 Supported Conversions

| Conversion   | Input   | Output  |
| ------------ | ------- | ------- |
| JSON → Excel | `.json` | `.xlsx` |
| Excel → JSON | `.xlsx` | `.json` |

---

## 📚 What I Learned

* How to work with JSON files in Python.
* How to read and write Excel files.
* How to use Pandas for data conversion.
* How to work with DataFrames.
* How structured JSON data can be represented as tabular data.
* How to convert data between different file formats.
* How to create reusable data-processing utilities.
* How to handle file-related errors.

---

## 🎯 Learning Outcome

This project helped me understand how Python and Pandas can be used to transform and exchange structured data between JSON and Excel formats.

It also improved my understanding of DataFrames and how they can be used as an intermediate structure when processing different types of data files.

---

## 📂 Project Structure

```text
Day_06/
│
├── 06_Day_06.py
├── input.json
├── output.xlsx
└── README.md
```

---

Part of my **10-Day Data Handling Python Projects Challenge** 📊🐍✨
