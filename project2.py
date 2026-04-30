import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import re

url = "http://books.toscrape.com/"

try:
    response = requests.get(url)
    response.encoding = 'utf-8'    
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print("Error fetching data:", e)
    exit()

soup = BeautifulSoup(response.text, "html.parser")
books = soup.find_all("article", class_="product_pod")
names = []
prices = []
for book in books:
    name = book.h3.a["title"]
    price_text = book.find("p", class_="price_color").text
    price = float(re.findall(r'\d+\.\d+', price_text)[0])
    names.append(name)
    prices.append(price)

df = pd.DataFrame({
    "Book Name": names,
    "Price": prices
})

print("\n Table Data:\n")
print(df.head())
df.to_csv("books_data.csv",index=False)
print("\n CSV File 'books_data.csv' created successfully!")

plt.figure()
plt.bar(names[:10],prices[:10])
plt.xticks(rotation=90)
plt.xlabel("Book Names")
plt.ylabel("Price")
plt.title("Book Prices(Top 10)")
plt.tight_layout()
plt.show()
