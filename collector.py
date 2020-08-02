import requests
from config import SIZE, LOCATION


class Collector:
    def __init__(self):
        self.location = LOCATION
        if SIZE > 1000:
            self.size = "1000"
            self.page = str(SIZE % 1000)
        else:
            self.size = str(SIZE)
        # penser à ajouter nb de page (page=) / penser params request dans dictonaire
        self.request = f"https://{self.location}.openfoodfacts.org/cgi/search.pl?action=process&page_size={self.size}&json=true"

    def collect(self) -> list:
        """Collect result from api request."""
        products = []
        r = requests.get(self.request)
        # Checking request status
        if r.status_code == requests.codes.ok:
            print("request ok")
        else:
            r.raise_for_status()
        # Adding result to list
        data = r.json()
        products = data.get("products")
        return products
