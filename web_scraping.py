import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website URL
url = "https://books.toscrape.com/"

# Send request
response = requests.get(url)

# Check if website loaded successfully
if response.status_code == 200:

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    book_names = []
    prices = []
    ratings = []

    for book in books:

        # Book Name
        name = book.h3.a["title"]

        # Price
        price = book.find("p", class_="price_color").text

        # Rating
        rating = book.find("p")["class"][1]

        book_names.append(name)
        prices.append(price)
        ratings.append(rating)

    # Create DataFrame
    data = pd.DataFrame({
        "Book Name": book_names,
        "Price": prices,
        "Rating": ratings
    })

    # Save into CSV
    data.to_csv("books_data.csv", index=False)

    print("Data Successfully Saved into books_data.csv")

    # Display first 10 rows
    print(data.head(10))

else:
    print("Website could not be loaded.")