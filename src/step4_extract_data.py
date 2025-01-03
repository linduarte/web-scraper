from bs4 import BeautifulSoup

# Sample HTML content (replace this with your actual HTML content)
html_content = """
<html>
<body>
<!-- Your HTML content here -->
</body>
</html>
"""

# Create a BeautifulSoup object
soup = BeautifulSoup(html_content, "html.parser")

# Find all book items on the page
books = soup.find_all("article", class_="product_pod")

for book in books:
    # Extract the title
    title = book.h3.a["title"]

    # Extract the price
    price = book.find("p", class_="price_color").text

    print(f"Title: {title}, Price: {price}")
