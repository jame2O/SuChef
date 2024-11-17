from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt


def scrape_items(item, stores):
    # Build URL
    stores_list = ""
    for store in stores:
        stores_list += f"{store}|"
    
    url = f"https://www.trolley.co.uk/search/?from=search&q={item}&stores_ids={stores_list}"
    print(stores)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html')

    # Create DF Table for consistent data storage
    
    df = pd.DataFrame(columns=['Brand', 'Description', 'ListPrice', 'UnitPrice', 'ImageURL'])
    
    # Scrape the data from the website using the search query, filter by results
    for data in (soup.find('section', id='search-results').find_all('div', class_='product-item')):
        imgUrl = f"https://www.trolley.co.uk{(data.find('div', class_='_img').find('img')['src'])}"
        info = data.find('div', class_='_info')
        brand = info.find('div', class_='_brand').string
        desc = info.find('div', class_='_desc').string
        price_div = info.find('div', class_='_price')
        listPrice = price_div.contents[1].strip() if len(price_div.contents) > 1 else None
        unitPrice = price_div.find('div', class_='_per-item').text.strip() if price_div.find('div', class_='_per-item') else None
        
        df = df._append({'Brand': brand, 'Description': desc, 'ListPrice': listPrice, 'UnitPrice': unitPrice, 'ImageURL': imgUrl}, ignore_index=True)
    
    return df.to_json(orient='records')

if __name__ == '__main__':
    table_of_stuff = scrape_items('milk', [2, 1])
    print(table_of_stuff)