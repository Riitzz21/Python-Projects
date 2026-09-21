# 📚 Day 03 - Books to Scrape (70 Books)

## 📌 Project Description

The **Books to Scrape (70 Books)** project is a Python web scraping application that collects information about books from the Books to Scrape website.

The project navigates through multiple pages and extracts useful information such as book titles, prices, ratings, and availability.

The collected information can then be displayed or stored for further analysis.

---

## 🚀 Features

- 🌐 Scrapes book information from a website
- 📚 Collects data for multiple books
- 📄 Handles multiple pages
- 🏷️ Extracts book titles
- 💰 Extracts book prices
- ⭐ Extracts book ratings
- 📦 Extracts availability information
- 📊 Organizes scraped data
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
- CSS Selectors
- Lists
- Dictionaries
- Loops
- Exception Handling
- Pagination

---

## 🔄 How It Works

```text
Books to Scrape Website
          ↓
     Send Request
          ↓
       Get HTML
          ↓
   BeautifulSoup Parser
          ↓
     Find Book Cards
          ↓
 ┌────────┼───────────┐
 ↓        ↓           ↓
Title    Price      Rating
          ↓
    Availability
          ↓
    Store 70 Books
```

---

## 📊 Data Collected

| Field | Description |
|---|---|
| Title | Name of the book |
| Price | Price of the book |
| Rating | Customer rating |
| Availability | Stock availability |

---

## 💻 Example Output

```text
===== Books to Scrape =====

1. A Light in the Attic
   Price: £51.77
   Rating: Three
   Availability: In stock

2. Tipping the Velvet
   Price: £53.74
   Rating: One
   Availability: In stock

3. Soumission
   Price: £50.10
   Rating: One
   Availability: In stock
```

The actual scraped results may change depending on the website content.

---

## 📚 What I Learned

- How to scrape repeated elements from a webpage.
- How to extract multiple attributes from HTML.
- How to work with CSS selectors.
- How to process multiple records using loops.
- How pagination works in web scraping.
- How to organize scraped data into Python structures.
- How to handle errors during web requests.
- How web scraping can be used for data collection.

---

## 🎯 Learning Outcome

This project helped me understand how to scrape structured information from multiple pages and collect multiple records efficiently.

It strengthened my understanding of BeautifulSoup, HTML parsing, pagination, loops, and structured data extraction.

---

## 📂 Project Structure

```text
Day_03/
│
├── 03_Day_03.py
└── README.md
```

---

Part of my **10-Day Web Scraping Python Projects Challenge** 🕷️🐍✨