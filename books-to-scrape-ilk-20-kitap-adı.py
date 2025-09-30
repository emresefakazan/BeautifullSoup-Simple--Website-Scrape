import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")

books = soup.find_all("article", class_="product_pod")

for book in books:
    title = book.h3.a["title"]   # <a> tag’inin "title" attribute’u
    print(title)
