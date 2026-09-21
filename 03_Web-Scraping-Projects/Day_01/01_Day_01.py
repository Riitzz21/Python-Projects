"""
Challenge : Scrape Wikipedia h2 Headers

Use the `requests` and `BeautifulSoup` libraries to fetch the Wikipedia 
page on Python (Programming Language).

Your task is to :
1. Downlaod the HTML of the page.
2. Parse all `<h2>` section headers.
3. Store the clean header titles in a list.
4. Print the total count and display the first 10 section titles.

Bonus :
- Remove any trailing "[edit]" from the headers.
- Handle network errors gracefully.

"""

import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/Python_(programming_language)"

def get_h2_headers(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to fetch page: \n {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    h2_tags = soup.find_all("h2")
    
    headers = []
    for tag in h2_tags:
        header_text = tag.get_text(strip=True)
        if header_text and header_text.lower() != "contents":
            headers.append(header_text)

    return headers


def main():

    while True:

        print("\n===== Wikipedia H2 Header Scraper =====")
        print("1. Scrape H2 Headers")
        print("2. Exit")

        choice =  input("Enter your choice : ").strip()

        match choice:

            case "1" : 
                headers = get_h2_headers(URL)

                if headers:
                    print("\n📌 H2 Headers:\n")

                    for i, header in enumerate(headers, 1):
                        print(f"{i}. {header}")

            case "2" :
                print("Goodbye! 👋") 
                break

            case _: 
                print("Invalid choice!") 
        
if __name__ == "__main__":
    main()