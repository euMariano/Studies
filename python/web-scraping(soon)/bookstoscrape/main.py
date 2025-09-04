import csv
import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/catalogue/category/books/philosophy_7/index.html"
pagina = requests.get(url)
soup = BeautifulSoup(pagina.text, "html.parser")

dados = soup.select("article.product_pod")

books = []

for i in dados:
    img = i.img["src"].split("/")[-1]
    title = i.h3.a["title"]
    price = i.find("p", {"class": "price_color"}).text
    price = price.replace("Â£", "")
    stock = i.select_one(".availability").get_text(strip=True)
    book = {"Title": title, "Price": price, "Stock": stock, "Image": img}
    books.append(book)

with open("books.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, books[0].keys())
    writer.writeheader()
    writer.writerows(books)
