import requests
from bs4 import BeautifulSoup

url = "https://www.udemy.com/sitemap/"
req = requests.get(url)
html = req.text
soup = BeautifulSoup(html, 'html.parser')

# Find all elements with class="row row-gap-md"
categories = soup.find_all('b')
categories_list = []

for category in categories:
    main_category = category.text.strip()
    subcategories = category.find_next('ul').find_all('a')

    category_dict = {
        'name': main_category,
        'id': '',  # Add the unique id for the main category
        'image_link': '',  # Add the image link for the main category
        'subcategories': []  # Initialize an empty list for subcategories
    }
    categories_list.append(category_dict)

    for subcategory in subcategories:
        subcategory_dict = {
            'name': subcategory.text,
            'id': '',  # Add the unique id for the subcategory
            'image_link': ''  # Add the image link for the subcategory
        }
        category_dict['subcategories'].append(subcategory_dict)

# Print the categories_list
for category in categories_list:
    for i , j in category.items():
        print(i, j)
    

    
    
