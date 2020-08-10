import requests
from config import SIZE, LOCATION


class Collector:
    def __init__(self):
        self.location = LOCATION
        self.size = str(SIZE)
        self.params = {"action": "process", "page_size": self.size, "json": "true"}
        self.request = f"https://{self.location}.openfoodfacts.org/cgi/search.pl?"

    def collect(self) -> list:
        """Collect result from api request."""
        products = []
        r = requests.get(self.request, self.params)
        # Checking request status
        if r.status_code == requests.codes.ok:
            print("request ok")
        else:
            r.raise_for_status()
        # Adding result to list
        data = r.json()
        products = data.get("products")
        return products
