# 🕷️ Day 05 - Download Cover Images Using `wget`

## 📌 Project Description

The **Download Cover Images Using `wget`** project is a Python web scraping application that extracts book cover image URLs from the **Books to Scrape** website and downloads the images locally using the `wget` library.

This project builds upon the previous web scraping projects by focusing on extracting image URLs and using an external Python package to download the corresponding files.

---

## 🚀 Features

* 🌐 Fetches book information from a website
* 📚 Extracts book cover image URLs
* 🖼️ Downloads cover images automatically
* 📥 Uses the `wget` Python library for downloading
* 📁 Saves downloaded images locally
* 🔢 Processes the required number of books/images
* ❌ Handles download-related errors

---

## 🛠️ Technologies & Libraries Used

* Python
* Requests
* BeautifulSoup
* wget
* HTML Parsing
* Web Scraping
* File Handling
* Exception Handling

---

## 🔄 How It Works

```text
Books to Scrape Website
          ↓
     Send HTTP Request
          ↓
       Get HTML
          ↓
  Parse with BeautifulSoup
          ↓
   Find Book Information
          ↓
 Extract Cover Image URL
          ↓
       wget Download
          ↓
    Save Image Locally
```

---

## 📊 Data Extracted

The project works with information such as:

| Data        | Description           |
| ----------- | --------------------- |
| Book Title  | Name of the book      |
| Image URL   | URL of the book cover |
| Cover Image | Downloaded image file |

---

## 📦 Installation

Make sure your virtual environment is activated.

Install the required packages:

```bash
python -m pip install requests beautifulsoup4 wget
```

Verify that `wget` is installed:

```bash
python -m pip show wget
```

---

## ▶️ How to Run

Run the Python program using:

```bash
python 05_Day_05.py
```

The program will scrape the required book cover URLs and download the images into the designated output folder.

---

## 📂 Project Structure

```text
Day_05/
│
├── 05_Day_05.py
├── README.md
│
└── book_covers/
    ├── book_cover_01.jpg
    ├── book_cover_02.jpg
    ├── book_cover_03.jpg
    └── ...
```

---

## 💻 Example Output

```text
===== Book Cover Downloader =====

Book 1: Downloading cover image...
✅ Image downloaded successfully.

Book 2: Downloading cover image...
✅ Image downloaded successfully.

Book 3: Downloading cover image...
✅ Image downloaded successfully.

...

🎉 Cover image downloading completed!
```

---

## 📚 What I Learned

* How to extract image URLs from HTML pages.
* How to use BeautifulSoup for web scraping.
* How to download files using the `wget` library.
* How to work with image URLs.
* How to save downloaded files locally.
* How to handle exceptions during web requests and downloads.
* How external Python packages can extend a web scraping project.

---

## 🎯 Learning Outcome

This project helped me understand how scraped information can be used to retrieve actual resources from the web.

It strengthened my knowledge of **BeautifulSoup, HTTP requests, URL extraction, file downloading, and the `wget` Python library**.

---

## 🔐 Note

This project was created for educational purposes as part of my **10-Day Web Scraping Python Projects Challenge**.

Web scraping should be performed responsibly while respecting the target website's terms, robots guidance, and reasonable request rates.

---

## 🐍 Challenge Progress

```text
Day 01 ✅ Scrape Wikipedia H2 Headers
Day 02 ✅ Hacker News Top Posts Scraper
Day 03 ✅ Scrape Books To Scrape (70 Books)
Day 04 ✅ Download Cover Images of First 10 Books
Day 05 ✅ Download Cover Images Using wget
Day 06 ⏳
Day 07 ⏳
Day 08 ⏳
Day 09 ⏳
Day 10 ⏳
```
