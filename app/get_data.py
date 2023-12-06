import requests
from bs4 import BeautifulSoup
import json

def setCatsUp():
    """
    Retrieves categories and subcategories from a website and saves them in a JSON file.

    Returns:
        tuple: A tuple containing a success message and the path to the JSON file.
    Usage:
        result, json_file_path = setCatsUp()
        print(result)
        print(json_file_path)
    """
    url = "https://www.udemy.com/sitemap/"
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    # Find all elements with class="row row-gap-md"
    categories = soup.find_all('b')
    categories_list = []
    category_id = 1  # Initialize the category ID counter

    for category in categories:
        main_category = category.text

        subcategories = category.find_next('ul').find_all('a')
        subcategory_id = 1  

        category_dict = {
            'name': main_category,
            'id': category_id,
            'image_link': '', 
            'type': 'parent',
            'subcategories': []  
        }
        categories_list.append(category_dict)
        
        for subcategory in subcategories:
            subcategory_dict = {
                'name': subcategory.text,
                'id': f"{subcategory_id}-{category_id}",
                'image_link': '',  
                'type': 'sub',
                'parent_id': category_dict['id']  
            }
            category_dict['subcategories'].append(subcategory_dict)
            subcategory_id += 1
        category_id += 1  
    json_path = 'categories.json'
    with open(json_path, 'w') as f:
        json.dump(categories_list, f, indent=4)

    return "Cats done", json_path

