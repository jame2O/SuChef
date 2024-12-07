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
        quant_tag = data.find('div', class_='_size')
        quant_no = data.find('div', class_='_qty')
        if quant_no is not None:
            
        else:
            unitSize = quant_tag.text    
        
        df = df._append({'Brand': brand, 
                         'Description': desc, 
                         'ListPrice': listPrice, 
                         'UnitQuantity': quantity,
                         'UnitPrice': price,
                         'UnitType': unit,
                         'Quantity': unitSize, 
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
    print (data)
    if 

def convert_units_to_metric(u1, u2):
    # We only need to have tables for liquid and solid metric measurements
    metric_liquid_factors = {
        'ml': 1,
        'l': 1000,
        'tsp': 4.92892,
        'tbsp': 14.7868,
        'fl oz': 29.5735,
        'cup': 240,
        'pint': 473.176,
        'quart': 946.353,
        'gallon': 3785.41,
    }
    metric_solid_factors = {
        'tsp': 4.92892,
        'tbsp': 14.7868,
        'oz': 29.5735,
        'lb': 453.592,
        'g': 1,
        'kg': 1000
    }
    
    if u2 in metric_liquid_factors.keys():
        return metric_liquid_factors[u1]
    
    if u2 in metric_solid_factors.keys():
        return metric_solid_factors[u1]
    
    raise ValueError(f"Unsupported units: {u1} or {u2}")

if __name__ == '__main__':
    item_data = get_all_named_item('onions', [1,2,3,4])
    jsonStr = item_data.to_json(orient='records', indent=4)
    with open(f'./api/data/grocery_data.json', 'w') as f:
        f.write(jsonStr)
    f.close()