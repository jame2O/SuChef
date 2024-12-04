from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import re
import json

def get_all_named_item(item, stores):
    # Build URL
    stores_list = ""
    for store in stores:
        stores_list += f"{store}|"
    
    url = f"https://www.trolley.co.uk/search/?from=search&q={item}&stores_ids={stores_list}"
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
        price, quantity, unit = extract_price_unit_quantity(unitPrice)
        unitSize = data.find('div', class_='_size').text
        
        df = df._append({'Brand': brand, 
                         'Description': desc, 
                         'ListPrice': listPrice, 
                         'UnitPrice': {
                             'price': price,
                             'quanity': quantity,
                             'unit': unit,
                         },
                         'UnitSize': unitSize, 
                         'ImageURL': imgUrl}, 
                        ignore_index=True)
    return tidy_data(df)
    

def extract_price_unit_quantity(price_string):
    # Define the regular expression pattern
    if price_string == None:
        return None, None, None
    pattern = r'£([\d\.]+) per (\d+)([a-zA-Z]+)'
    
    # Search for the pattern in the price string
    match = re.search(pattern, price_string)
    
    if match:
        price = float(match.group(1))
        quantity = int(match.group(2))
        unit = match.group(3)
        return price, quantity, unit
    else:
        return None, None, None
    
    
def tidy_data(data):
    # TODO
    return data


if __name__ == '__main__':
    item_data = get_all_named_item('onions', [1,2,3,4])
    jsonStr = item_data.to_json(orient='records', indent=4)
    with open(f'./api/data/grocery_data.json', 'w') as f:
        f.write(jsonStr)
    f.close()