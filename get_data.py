import requests
from bs4 import BeautifulSoup
import json
import base64
from dataclasses import dataclass, fields
from dataclasses import dataclass, fields
import requests
from app import app, db, migrate

from app.models import Category, Courses, SubCategory

client_id= 'vPMELH5fShlp2e0UFbyzCQKGItjcmoL8xR0hfZXl'
client_secret= '6xUpSdCcYP170BpSE9dQczzZDt5L8A7f583K2AQE67u1Bqjt0utUVtunaiUhydbpLNV5sPfwLTd5tPimi58WdRWL2zB12tdns888naZ5VlTM0Ujsi1WavR0UoaA7JPVk',
    
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

@dataclass
class UdemyApiParams:
    page: int = 1
    page_size: int = 1
    search: str = ''
    category: str = ''
    subcategory: str = ''
    price: str = ''
    is_affiliate_agreed: bool = False
    is_deals_agreed: bool = True
    ratings: int = 5

    def __str__(self):
        return '&'.join([f"{field.name}={getattr(self, field.name)}" for field in fields(self) if len(str(getattr(self, field.name))) > 0])



def getCourses(params: UdemyApiParams = None):
    param = {
        'client_id': 'vPMELH5fShlp2e0UFbyzCQKGItjcmoL8xR0hfZXl',
        'client_secret': '6xUpSdCcYP170BpSE9dQczzZDt5L8A7f583K2AQE67u1Bqjt0utUVtunaiUhydbpLNV5sPfwLTd5tPimi58WdRWL2zB12tdns888naZ5VlTM0Ujsi1WavR0UoaA7JPVk',
    }

    base_url = "https://www.udemy.com/api-2.0"
    auth_string = f"{param['client_id']}:{param['client_secret']}"
    auth_header = base64.b64encode(auth_string.encode()).decode("utf-8")
    headers = {"Authorization": f"Basic {auth_header}"}
    end_point = '/courses'

    if params:
        query_params = str(params)
        url = f"{base_url}{end_point}/?{query_params}"
    else:
        url = f"{base_url}{end_point}"

    response = requests.get(url, headers=headers)
    # print(url)
    # print(query_params)
    if response.status_code == 200:
        course_data = response.json()
        return course_data
    else:
        print(f"Error: {response.status_code}")
        return None

#^--> 0- this is the first to run on the server
# setCatsUp()

# # Example usage for getCourses()
# # params = UdemyApiParams(category='Development',page_size=2,subcategory='Web Development',search='python')
# # courses_data = getCourses(params)
# # if courses_data:
# #     print(courses_data['results'])

#^---> 1 - migrate the database to the latest version
#! this is the secound to run on the server
# with app.app_context():
#     db.create_all()
#     migrate.init_app(app, db)
#     db.session.commit()

#~ if you want to upgrade with new columns run this 


# flask db init  
# flask manage.py db migrate -m "commit msg"
# flask manage.py db upgrade

# #^ --> 2- add categories from json to the database

with app.app_context():
    with open('categories.json', 'r') as f:
        categories = json.load(f)
        for category in categories:
            existing_cat = db.session.get(Category, category['id'])
            if not existing_cat:
                cat = Category(
                    id=category['id'],
                    title=category['name'],
                    slug=category['name'].replace(' ', '-'),
                    url='',
                    image='',
                    types='parent',
                )
                db.session.add(cat)
                db.session.commit()

                for subcategory in category['subcategories']:
                    existing_subcat = db.session.get(SubCategory, subcategory['id'])
                    if not existing_subcat:
                        subcat = SubCategory(
                            id=subcategory['id'],
                            title=subcategory['name'],
                            slug=subcategory['name'].replace(' ', '-'),
                            url='',
                            image='',
                            types='sub',
                            parent_id=category['id'],
                        )
                        db.session.add(subcat)
                        db.session.commit()









