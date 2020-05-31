import requests
import json

def collect(request):
    
    r = requests.get(request)
    products = []
    data = json.loads(r.text)
    products = data['products']

    return products


request = 'https://fr.openfoodfacts.org/cgi/search.pl?action=process&page_size=5&json=true'
products = collect(request)