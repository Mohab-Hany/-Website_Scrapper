import requests
from bs4 import BeautifulSoup


def get_books():
    url = "https://books.toscrape.com/"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")
        books = soup.find_all("article", class_="product_pod")

        for number, book in enumerate(books, start=1):
            title = book.h3.a.get("title", "Unknown")
            rating = book.p.get("class", ["", "Unknown"])[1]
            price = book.find("p", class_="price_color").text.strip()

            print(f"{number}. Book: {title}")
            print(f"   Rating: {rating} Star")
            print(f"   Price : {price}")
            print("-" * 50)

    except requests.exceptions.RequestException as error:
        print(f"An error occurred: {error}")


# تشغيل البرنامج
get_books()