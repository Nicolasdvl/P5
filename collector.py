import requests
from config import size, location

class Collector :     
    
    def __init__(self):
        self.location = location
        if size > 1000 :
            self.size = '1000'
            self.page = str(size % 1000)
        else :
            self.size = str(size)
        
        ''' penser à ajouter nb de page (page=) / penser params request dans dictonaire '''
        self.request = f'https://{self.location}.openfoodfacts.org/cgi/search.pl?action=process&page_size={self.size}&json=true'  

    def collect(self):
        
        products = []
        r = requests.get(self.request)

        ''' penser à check le status de la request (error 400 etc)'''
        data = r.json()
        products = data['products']

        return products

