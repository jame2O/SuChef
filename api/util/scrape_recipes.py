from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import json
import unicodedata

COLLECTION_NAMES = [['november-recipes', 2]]
fraction_chars = {'\u00BD', '\u00BC', '\u00BE', '\u2150', '\u2151', '\u2152', '\u2153', '\u2154', 
                  '\u2155', '\u2156', '\u2157', '\u2158', '\u2159', '\u215A', '\u215B', '\u215C', 
                  '\u215D', '\u215E'}
def scrape_bbc_links(collection_name, pages):
    links = []
    for i in range(1, pages+1):
        url = f"https://www.bbcgoodfood.com/recipes/collection/{collection_name}?page={i}"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html')
        
        for data in (soup.find_all('div', class_='card__content')):
            link = data.find('a')['href']
            if link.startswith('/recipes/'):
                links.append(link)
    return links   

def scrape_bbc_recipes(links):
    data = []
    for link in links:
        recipe_data = {
            "name": None,
            "prep_time": None,
            "cook_time": None,
            "image_url": None,
            "ingredients": [],
            "method": [],
        }
        url = f"https://www.bbcgoodfood.com{link}"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html')
        ## Recipe name
        recipe_name = soup.find('h1', class_='heading-1').text.strip()
        recipe_data["name"] = recipe_name
        ## Prep info
        header_image_container = soup.find('div', class_="post-header__image-container")
        if header_image_container is not None:
            image_url = header_image_container.find('img', class_="image__img").attrs["src"]
            recipe_data['image_url'] = image_url
        else:
            recipe_data['image_url'] = "n/a"
        time_elements = soup.find_all('time')
        for time_element in time_elements:
            if 'Prep:' in time_element.find_previous('span').find_previous('span').text:
                recipe_data['prep_time'] = time_element.text.strip()
            elif 'Cook:' in time_element.find_previous('span').find_previous('span').text:
                recipe_data['cook_time'] = time_element.text.strip()
        
        data.append(recipe_data)
        ## Image url
        
        ## Ingredients info
        
        ing_list_html = soup.find('div', class_='tabbed-list__content').find('ul', class_="ingredients-list")        
        # Regular expressions for extracting quantity and units
        for ing in ing_list_html.find_all('li'):
            ingredient = {
                "name": None,
                "quantity": None,
                "notes": None
            }
            # Split up ingreditent into quantity & unit, name & notes if any
            if ing.find('div', class_='ingredients-list__item-note') is not None:
                ingredient["notes"] = ing.find('div', class_='ingredients-list__item-note').text.strip()
                
            if ing.find('a') is not None:
                ingredient["name"] = ing.find('a').text.strip()
                if ing.contents[0] is not None and isinstance(ing.contents[0], str):
                    quantity_data = ing.contents[0].strip()
                    ingredient["quantity"] = extract_price_unit_quantity(quantity_data)
            elif len(ing.contents) > 2:
                quantity_data = ing.contents[0].strip()
                ingredient["quantity"] = extract_price_unit_quantity(quantity_data)
                if isinstance(ing.contents[2],str):
                    ingredient["name"] = ing.contents[2].strip()
            else:
                ingredient["name"] = ing.contents[0].strip()
            recipe_data["ingredients"].append(ingredient)
        
        ## Method info
        step_count = 1
        method_html = soup.find('ul', class_="method-steps__list")
        for method in method_html.find_all('li'):
            text = method.find('p').text.strip()
            recipe_data["method"].append({
                "step": step_count,
                "text": text
            })
            step_count += 1
        data.append(recipe_data)

    return data

# Extract quantity, unit & some cleaning (fractions)        
def extract_price_unit_quantity(price_string):
    # Define the regular expression pattern
    if price_string == None:
        return None
    pattern = r'((\d+(\.\d+)?)?([\u00BC-\u00BE\u2150-\u215E])?)(\s*)(lb|ml|g|kg|tsp|tbsp|oz|l|fl\.oz|fl oz|floz)?(?=\s|$)(\s*[a-zA-Z\s]*)?'
    # Search for the pattern in the price string
    match = re.search(pattern, price_string)
    
    if match:
        quantity = (match.group(1))
        unit = ""
        if match.group(6):
            unit = (match.group(6))
        else:
            unit = match.group(7)
        if quantity is not None:
            quantity = parse_quant(quantity)
        
        return {
            "quantity": quantity,
            "unit": unit
        }
    else:
        return price_string
def parse_quant(text):
    parts = list(text)
    for char in fraction_chars:
        if char in parts:
            # Just a fraction
            if len(parts) == 1:
                return unicodedata.numeric(parts[0])
            else:
                whole_n = int(parts[0])
                fraction = unicodedata.numeric(parts[1])
                return whole_n + fraction
    if text.isnumeric():
        return int(text)
    else:
        return text
            
    
if __name__ == '__main__':
    total_data = []
    for names in COLLECTION_NAMES:
        links = scrape_bbc_links(names[0], names[1])
        next_data = scrape_bbc_recipes(links)
        total_data.append({
            "source": "bbc_good_food",
            "collection": names[0],
            "data": next_data
        })
        
    with open(f'./api/data/test_data.json', 'w') as f:
        json.dump(total_data, f, indent=4)