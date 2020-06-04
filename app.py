from models import product, store, category
from config import uri, request
from sqlalchemy import *
from collect import Collect
from cleaner import Cleaner

engine = create_engine(uri)

product.Base.metadata.create_all(engine)
category.Base.metadata.create_all(engine)
store.Base.metadata.create_all(engine)



products = Collect.collect(request)
table_data = Cleaner.cleaner_prod(products)
table_cat = Cleaner.cleaner_cat(products)
table_store = Cleaner.cleaner_store(products)

print(table_data)
