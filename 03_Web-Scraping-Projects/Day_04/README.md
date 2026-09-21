# 📚 Day 04 - Download Cover Images of First 10 Books

## 📌 Project Description

The **Download Cover Images of First 10 Books** project is a Python web scraping application that extracts the cover image URLs of the first 10 books from the **Books to Scrape** website and downloads the images locally.

The project combines web scraping with file downloading and demonstrates how Python can retrieve resources from the web and save them to a local directory.

---

## 🚀 Features

- 🌐 Scrapes book information from a website
- 📚 Extracts the first 10 books
- 🖼️ Extracts book cover image URLs
- 📥 Downloads cover images automatically
- 📁 Creates a local folder for downloaded images
- 🏷️ Saves images with organized filenames
- ❌ Handles request and download errors

---

## 🛠️ Technologies & Concepts Used

- Python
- Requests
- BeautifulSoup
- HTML Parsing
- Web Scraping
- HTTP Requests
- Image Downloading
- File Handling
- Lists
- Loops
- Exception Handling
- URL Handling

---

## 🔄 How It Works

```text
Books to Scrape Website
          ↓
     Send HTTP Request
          ↓
       Get HTML
          ↓
   BeautifulSoup Parser
          ↓
     Find First 10 Books
          ↓
    Extract Image URLs
          ↓
    Send Image Requests
          ↓
     Download Images
          ↓
     Save Locally
```

---

## 📊 Data Collected

For each book, the program extracts:

| Data | Description |
|------|-------------|
| Book Title | Title of the book |
| Image URL | URL of the book cover |
| Cover Image | Downloaded image file |

---

## 📂 Downloaded Images

The downloaded cover images are stored inside the `book_covers` folder.

Example:

```text
book_covers/
│
├── 01_book_cover.jpg
├── 02_book_cover.jpg
├── 03_book_cover.jpg
├── 04_book_cover.jpg
├── 05_book_cover.jpg
├── 06_book_cover.jpg
├── 07_book_cover.jpg
├── 08_book_cover.jpg
├── 09_book_cover.jpg
└── 10_book_cover.jpg
```

---

## 💻 Example Output

```text
===== Book Cover Downloader =====

Found: A Light in the Attic
Downloading cover image...

Found: Tipping the Velvet
Downloading cover image...

Found: Soumission
Downloading cover image...

...

✅ Successfully downloaded 10 book cover images.
```

---

## 📚 What I Learned

- How to extract image URLs from HTML.
- How to work with `<img>` elements using BeautifulSoup.
- How to retrieve images using the Requests library.
- How to save downloaded files locally.
- How to create directories using Python.
- How to handle HTTP and file-related errors.
- How web scraping can be combined with file downloading.
- How to organize downloaded resources.

---

## 🎯 Learning Outcome

This project helped me understand how scraped data can be used to retrieve additional resources from a webpage.

It strengthened my understanding of HTML parsing, image URL extraction, HTTP requests, file handling, and automated downloading.

---

## 📂 Project Structure

```text
Day_04/
│
├── 04_Day_04.py
├── book_covers/
│   ├── 01_book_cover.jpg
│   ├── 02_book_cover.jpg
│   ├── ...
│   └── 10_book_cover.jpg
│
└── README.md
```

---

## 🔐 Note

This project is created for educational purposes as part of my web scraping practice.

The scraper should be used responsibly and in accordance with the website's terms and applicable rules.

---

Part of my **10-Day Web Scraping Python Projects Challenge** 🕷️🐍✨