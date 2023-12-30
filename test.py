from dotenv import load_dotenv

load_dotenv()

# print all var from venv

import os

for k, v in os.environ.items():
    print(f'{k}={v}')
    
