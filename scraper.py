import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://books.toscrape.com/catalogue/page-{}.html"

books = []

for page in range(1, 6):  # Pagination (5 pages)
    try:
        response = requests.get(base_url.format(page), timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        articles = soup.find_all("article", class_="product_pod")

        for book in articles:
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text.replace("£", "")
            rating = book.p["class"][1]
            availability = book.find("p", class_="instock availability").text.strip()

            books.append([title, price, rating, availability])

    except Exception as e:
        print(f"Error on page {page}: {e}")

df = pd.DataFrame(books, columns=["Title", "Price", "Rating", "Availability"])
df.to_csv("books_raw.csv", index=False)

print("✅ Scraping Completed. File saved as books_raw.csv")
