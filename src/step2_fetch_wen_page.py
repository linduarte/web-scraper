import requests

url = "http://books.toscrape.com/"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print("Successfully fetched the page!")
    page_content = response.content
else:
    print("Failed to retrieve the page")
