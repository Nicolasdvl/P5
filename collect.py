import requests
import json
class Collect ():     
    
    def collect(request):
        
        products = []
        r = requests.get(request)
        data = json.loads(r.text)
        products = data['products']

        return products

