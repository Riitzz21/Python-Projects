# 📰 Day 02 - Hacker News Top Posts Scraper

## 📌 Project Description

The **Hacker News Top Posts Scraper** is a Python web scraping application that collects information about top posts from the Hacker News website.

The project sends an HTTP request to the webpage, parses the HTML using BeautifulSoup, and extracts useful information such as post titles, links, and scores.

---

## 🚀 Features

- 🌐 Scrapes Hacker News webpage
- 📡 Sends HTTP requests using Python
- 🥣 Parses HTML using BeautifulSoup
- 📰 Extracts post titles
- 🔗 Extracts post links
- ⭐ Extracts post scores
- 📊 Displays scraped posts in a clean format
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
- Exception Handling

---

## 🔄 How It Works

```text
Hacker News Webpage
        ↓
   HTTP Request
        ↓
     HTML Data
        ↓
 BeautifulSoup Parser
        ↓
 Find Post Elements
        ↓
Extract Title / Link / Score
        ↓
 Display Top Posts
```

---

## 📊 Data Collected

The scraper collects information such as:

| Data | Description |
|------|-------------|
| Title | Name of the Hacker News post |
| Link | URL associated with the post |
| Score | Number of points received by the post |

---

## 💻 Example Output

```text
===== Hacker News Top Posts =====

1. A New Programming Tool
   Score: 245
   Link: https://example.com/article

2. Understanding Python
   Score: 198
   Link: https://example.com/python

3. Building Better Software
   Score: 156
   Link: https://example.com/software
```

The actual results may change because Hacker News content is updated continuously.

---

## 📚 What I Learned

- How to scrape information from a real website.
- How to locate specific HTML elements.
- How to extract multiple pieces of information from a webpage.
- How to work with HTML attributes.
- How to use BeautifulSoup for structured web scraping.
- How to handle HTTP request errors.
- How scraped data can be organized and displayed.

---

## 🎯 Learning Outcome

This project helped me move beyond extracting simple HTML elements and understand how to collect structured information from multiple elements on a real-world webpage.

It strengthened my understanding of HTTP requests, HTML parsing, BeautifulSoup, and web data extraction.

---

## 📂 Project Structure

```text
Day_02/
│
├── 02_Day_02.py
└── README.md
```

---

Part of my **10-Day Web Scraping Python Projects Challenge** 🕷️🐍✨