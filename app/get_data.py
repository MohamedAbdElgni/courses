import requests
from bs4 import BeautifulSoup

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
    category_id += 1  

    for subcategory in subcategories:
        subcategory_dict = {
            'name': subcategory.text,
            'id': f"{category_id}-{subcategory_id}",
            'image_link': '',  
            'type': 'sub',
            'parent_id': category_dict['id']  
        }
        category_dict['subcategories'].append(subcategory_dict)
        subcategory_id += 1  


# for category in categories_list:
#     for i, j in category.items():
#         print(i, j)

# add this data to json file

import json

with open('categories.json', 'w') as f:
    json.dump(categories_list, f, indent=4)



