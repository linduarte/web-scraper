import csv

import requests
from bs4 import BeautifulSoup


def scrape_books_to_csv(url, csv_file):
    with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Price"])  # Write the header row

        while url:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")

            books = soup.find_all("article", class_="product_pod")
            for book in books:
                title = book.h3.a["title"]
                price = book.find("p", class_="price_color").text
                writer.writerow([title, price])

            next_page = soup.find("li", class_="next")
            if next_page:
                url = "http://books.toscrape.com/catalogue/" + next_page.a["href"]
            else:
                url = None


# Start scraping and saving data
scrape_books_to_csv("http://books.toscrape.com/", "D:/2024/MLOPs/23102024/books.csv")


def scrape_books_to_csv(url, csv_file):
    with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Price"])  # Write the header row

        while url:
            response = requests.get(url)

            # Ensure that the encoding is set correctly
            response.encoding = "utf-8"  # Fix encoding to handle special characters

            soup = BeautifulSoup(response.content, "html.parser")

            books = soup.find_all("article", class_="product_pod")
            for book in books:
                title = book.h3.a["title"]
                price = book.find("p", class_="price_color").text.strip()
                writer.writerow([title, price])

            # Check if there's a next page
            next_page = soup.find("li", class_="next")
            if next_page:
                url = "http://books.toscrape.com/catalogue/" + next_page.a["href"]
            else:
                url = None


# Start scraping and saving data
scrape_books_to_csv("http://books.toscrape.com/", "D:/2024/23102024/books.csv")
