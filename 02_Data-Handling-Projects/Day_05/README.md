# 🌦️ Day 05 - Real-Time Weather Logger (API + CSV)

## 📌 Project Description

The **Real-Time Weather Logger** is a Python application that collects real-time weather information using a weather API and stores the collected data in a CSV file.

The project demonstrates how Python can fetch data from an external API, process JSON responses, and maintain a historical weather log using CSV file handling.

---

## 🚀 Features

* 🌍 Fetches real-time weather information using an API
* 🌡️ Retrieves temperature information
* ☁️ Retrieves current weather conditions
* 📊 Processes data received from the API
* 💾 Stores weather records in a CSV file
* 📅 Maintains a history of weather observations
* 📈 Visualizes temperature and weather conditions
* 🖥️ Uses a simple command-line interface

---

## 🔄 How It Works

```text
User enters location
        ↓
Python sends API request
        ↓
Weather API returns JSON data
        ↓
Program extracts required information
        ↓
Weather data is stored in CSV
        ↓
CSV data is read and analyzed
        ↓
Matplotlib generates visualizations
```

---

## 🛠️ Technologies & Concepts Used

* Python
* CSV File Handling
* JSON Data
* API Requests
* Dictionaries
* Lists
* `csv.DictReader`
* `defaultdict`
* Matplotlib
* Functions
* Exception Handling
* Data Visualization
* File Handling

---

## 📊 Data Storage

Weather information is stored in a CSV file.

Example structure:

```csv
Date,Temperature,Condition
2026-08-10,28.5,Sunny
2026-08-11,27.2,Cloudy
2026-08-12,29.1,Rainy
```

The CSV file allows multiple weather observations to be stored and analyzed later.

---

## 📈 Data Visualization

The project generates visualizations from the stored weather data.

### 🌡️ Temperature Over Time

A line chart is used to visualize how temperature changes across different dates.

### ☁️ Weather Conditions

A bar chart is used to show how frequently different weather conditions occur in the collected data.

---

## 📚 What I Learned

* How to work with external APIs in Python.
* How API responses are commonly provided as JSON.
* How to extract useful information from structured data.
* How to store API data in CSV files.
* How to read and process CSV data using `csv.DictReader`.
* How to use `defaultdict` for counting weather conditions.
* How to create charts using Matplotlib.
* How to handle missing or invalid data.
* How to visualize real-world data.

---

## 🎯 Learning Outcome

This project helped me understand how Python can collect real-world data from an external API, store it in a structured CSV format, process the stored data, and create visualizations for analysis.

---

## 🔐 Security Note

The API key used by the project should **never be uploaded to GitHub**.

Sensitive information such as API keys should be stored using environment variables or a `.env` file and added to `.gitignore`.

---

## 📂 Project Structure

```text
Day_05/
│
├── 05_Day_05.py
├── weather_logs.csv
└── README.md
```

---

Part of my **10-Day Data Handling Python Projects Challenge** 📊🐍✨
