import requests
import json

def collect(request):
    
    r = requests.get(request)
    products = []
    data = json.loads(r.text)
    products = data['products']

    return products

def clean_for_data(list):

    table = []
    for pos, element in enumerate(list):
        table.append((list[pos]["product_name"], list[pos]["ingredients_text_fr"], list[pos]["labels"], list[pos]["nutriscore_grade"]))
    return table   

def clean_for_categories(list):

    table = []
    for pos, element in enumerate(list):
        table.append((list[pos]["product_name"], list[pos]["ingredients_text_fr"], list[pos]["labels"], list[pos]["nutriscore_grade"]))
    return table  
