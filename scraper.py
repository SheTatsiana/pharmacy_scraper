
import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "http://camelia.lt/"
response = requests.get(URL)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    products = []

    for product in soup.find_all('div', class_='product'):
        name = product.find('h3').text
        price = product.find('span', class_='price').text
        availability = product.find('p', class_='availability').text.strip()
        products.append({
            'Name': name,
            'Price': price,
            'Availability': availability
        })

    df = pd.DataFrame(products)
    df.to_csv('pharmacy_products.csv', index=False)
    print("Data has been written to pharmacy_products.csv")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
