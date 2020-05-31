from models import data, stores, categories
from config import uri
from sqlalchemy import *
from collect import collect
from clean import clean_for_data, clean_for_cat, clean_for_store

engine = create_engine(uri)

data.Base.metadata.create_all(engine)
categories.Base.metadata.create_all(engine)
stores.Base.metadata.create_all(engine)


request = 'https://fr.openfoodfacts.org/cgi/search.pl?action=process&page_size=5&json=true'
products = collect(request)
table_data = clean_for_data(products)
table_cat = clean_for_cat(products)
table_store = clean_for_store(products)

print(table_cat)
