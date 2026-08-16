# 🔐 Day 09 - Offline Credential Manager

## 📌 Project Description

The **Offline Credential Manager** is a Python command-line application designed to store and manage login credentials locally.

The project allows users to add, view, search, update, and delete credential records while storing the data in a local file. It demonstrates how Python can be used to manage structured data and introduces basic concepts related to protecting sensitive information.

---

## 🚀 Features

* ➕ Add new credentials
* 📋 View saved credentials
* 🔍 Search for stored credentials
* ✏️ Update existing credentials
* 🗑️ Delete credentials
* 💾 Store credential data locally
* 🔐 Keeps data offline
* 🖥️ Command-line interface
* ❌ Handles invalid input and file-related errors

---

## 🛠️ Technologies & Concepts Used

* Python
* JSON
* File Handling
* Dictionaries
* Lists
* Functions
* Loops
* Conditional Statements
* Exception Handling
* Data Validation
* Local Data Storage

---

## 🔄 How It Works

```text
User
  ↓
Select an Operation
  ↓
┌───────────────┐
│ Add Credential│
│ View Records  │
│ Search        │
│ Update        │
│ Delete        │
└───────────────┘
  ↓
Local Storage
  ↓
Credentials Retrieved / Updated
```

---

## 📊 Example Data Structure

```json
[
    {
        "website": "example.com",
        "username": "user123",
        "password": "********"
    }
]
```

---

## 📚 What I Learned

* How to store structured data locally.
* How to work with JSON-based data storage.
* How to implement CRUD operations.
* How to search and update stored records.
* How to validate user input.
* How to handle file-related exceptions.
* How local data storage can be used in Python applications.
* Why sensitive information should be handled carefully.

---

## 🔐 Security Note

This project is created for **educational purposes** and should not be treated as a production-ready password manager.

Real-world credential managers should use strong encryption, secure key management, protected storage, and additional security mechanisms.

**Never upload real passwords, API keys, or personal credentials to GitHub.**

---

## 📂 Project Structure

```text
Day_09/
│
├── 09_Day_09.py
├── credentials.json
└── README.md
```

---

## 🎯 Learning Outcome

This project helped me understand how Python can manage structured local data while introducing important concepts related to handling sensitive information.

It strengthened my understanding of file handling, JSON, CRUD operations, data validation, and secure-data awareness.

---

Part of my **10-Day Data Handling Python Projects Challenge** 📊🐍✨
