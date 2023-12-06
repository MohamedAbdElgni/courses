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
    subcategory_id = 1  # Initialize the subcategory ID counter

    category_dict = {
        'name': main_category,
        'id': category_id,
        'image_link': '',  # Add the image link for the main category
        'subcategories': []  # Initialize an empty list for subcategories
    }
    categories_list.append(category_dict)
    category_id += 1  # Increment the category ID counter

    for subcategory in subcategories:
        subcategory_dict = {
            'name': subcategory.text,
            'id': f"{category_id}-{subcategory_id}",
            'image_link': '',  # Add the image link for the subcategory
            'parent_id': category_dict['id']  # Add the id of the main category
        }
        category_dict['subcategories'].append(subcategory_dict)
        subcategory_id += 1  # Increment the subcategory ID counter

# Print the categories_list
for category in categories_list:
    for i, j in category.items():
        print(i, j)
    

