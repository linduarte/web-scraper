import requests
from bs4 import BeautifulSoup


def scrape_books_from_page(url):
    while url:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        # Scrape book titles and prices
        books = soup.find_all("article", class_="product_pod")
        for book in books:
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text
            print(f"Title: {title}, Price: {price}")

        # Find and follow the "Next" page link
        next_page = soup.find("li", class_="next")
        if next_page:
            next_url = next_page.a["href"]
            # Construct full URL for the next page
            url = "http://books.toscrape.com/catalogue/" + next_url
        else:
            url = None  # No more pages to scrape


# Start scraping from the first page
start_url = "http://books.toscrape.com/catalogue/page-1.html"
scrape_books_from_page(start_url)
