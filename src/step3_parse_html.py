from bs4 import BeautifulSoup

page_content = "<html></html>"  # Define page_content with some HTML content
soup = BeautifulSoup(page_content, "html.parser")
print(soup.prettify())  # This prints the formatted HTML
