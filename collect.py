import requests
import json
class Collect ():
    def __init__(self):

        self.request = 'https://fr.openfoodfacts.org/cgi/search.pl?action=process&page_size=5&json=true'
        
    
    def collect(request):
        
        products = []
        r = requests.get(request)
        data = json.loads(r.text)
        products = data['products']

        return products

