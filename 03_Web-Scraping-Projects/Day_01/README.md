# 🌐 Day 01 - Scrape Wikipedia H2 Headers

## 📌 Project Description

The **Scrape Wikipedia H2 Headers** project is a beginner-friendly Python web scraping application that extracts all `<h2>` headings from a Wikipedia webpage.

The project sends an HTTP request to the webpage, parses the returned HTML using BeautifulSoup, identifies the `<h2>` elements, and displays their text in the terminal.

---

## 🚀 Features

- 🌐 Fetches a Wikipedia webpage
- 📡 Sends an HTTP request using Python
- 🥣 Parses HTML using BeautifulSoup
- 🔎 Finds all `<h2>` elements
- 📝 Extracts and displays heading text
- ❌ Handles request-related errors

---

## 🛠️ Technologies & Concepts Used

- Python
- Requests
- BeautifulSoup
- HTML
- Web Scraping
- HTTP Requests
- HTML Parsing
- CSS/HTML Selectors
- Exception Handling

---

## 🔄 How It Works

```text
Wikipedia Webpage
       ↓
   HTTP Request
       ↓
    HTML Data
       ↓
 BeautifulSoup Parser
       ↓
 Find <h2> Elements
       ↓
 Extract Heading Text
       ↓
 Display Results
```

---

## 💻 Example

The program extracts headings such as:

```text
Contents
History
Geography
Economy
Culture
References
```

The exact headings depend on the Wikipedia page being scraped.

---

## 📚 What I Learned

- How HTTP requests work in Python.
- How to retrieve HTML from a webpage.
- How to use the `requests` library.
- How to parse HTML using BeautifulSoup.
- How HTML elements such as `<h2>` can be located.
- How to extract text from HTML elements.
- How to handle errors when making web requests.

---

## 🎯 Learning Outcome

This project helped me understand the basic workflow of web scraping:

**Request → Parse → Find → Extract → Display**

It provided a foundation for building more advanced web scraping projects.

---

## 📂 Project Structure

```text
Day_01/
│
├── 01_Day_01.py
└── README.md
```

---

Part of my **10-Day Web Scraping Python Projects Challenge** 🕷️🐍✨