import requests
from bs4 import BeautifulSoup
import csv

# URL of the page to scrape
url = "https://vapi.eumetsat.int/data/browse/1.0.0/collections/EO%3AEUM%3ADAT%3AMETOP%3ASOMO12/dates/2020/04/08/products?format=html"

# Send a GET request to the URL
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all product identifiers on the page
products = soup.find_all('a')

# Extract product names and details
product_list = []
for product in products:
    name = product.text.strip()
    if name.startswith("ASCA"):
        link = product['href']
        product_list.append([name, link])

# Find the total number of products at the bottom of the page
total_products_text = soup.find(text=lambda text: text and "Total:" in text)
total_products = int(total_products_text.split(":")[1].strip())

# Write results to a CSV file
with open('products_2020_04_08.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Product Name", "Product Link"])
    writer.writerows(product_list)
    writer.writerow(["Total Products", total_products])

print(f"Found {len(product_list)} products. Results written to products_2020_04_08.csv")