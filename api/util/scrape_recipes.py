from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import matplotlib.pyplot as plt
import json

COLLECTION_NAMES = [['november-recipes', 4], ['student-recipes', 5],['salad-recipes', 9], ['pasta-recipes', 5]]
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

        time_elements = soup.find_all('time')
        for time_element in time_elements:
            if 'Prep:' in time_element.find_previous('span').find_previous('span').text:
                recipe_data['prep_time'] = time_element.text.strip()
            elif 'Cook:' in time_element.find_previous('span').find_previous('span').text:
                recipe_data['cook_time'] = time_element.text.strip()
        
        data.append(recipe_data)
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
                    ingredient["quantity"] = ing.contents[0].strip()
            elif len(ing.contents) > 2:
                ingredient["quantity"] = ing.contents[0].strip()
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
        
        
if __name__ == '__main__':
    total_data = []
    for names in COLLECTION_NAMES:
        links = scrape_bbc_links(names[0], names[1])
        next_data = scrape_bbc_recipes(links)
        total_data.append({
            "collection": names[0],
            "data": next_data
        })
        
    with open(f'yummers.json', 'w') as f:
        json.dump(total_data, f, indent=4)