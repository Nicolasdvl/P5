from models import product, store, category
from config import uri
from sqlalchemy import *
from collect import Collect
from cleaner import cleaner_prod, cleaner_cat, cleaner_store

engine = create_engine(uri)

product.Base.metadata.create_all(engine)
category.Base.metadata.create_all(engine)
store.Base.metadata.create_all(engine)


request = Collect()
products = Collect.collect(request.request)
table_data = cleaner_prod(products)
table_cat = cleaner_cat(products)
table_store = cleaner_store(products)

print(table_data)
