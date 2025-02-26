import json
import os
from datetime import datetime

def get_next_business_id():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as file:
            try:
                businesses = json.load(file)
                if businesses:
                    last_id = businesses[-1]["id"]
                    next_id = int(last_id[1:]) + 1
                    return f"{next_id:d}"
            except json.JSONDecodeError:
                pass
    return "1" #Default if empty

def create_business():
    business_id = get_next_business_id()
    b_name = input("Enter Business Name: ")
    date_initialized = 
