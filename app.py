from models import product, store, category
from config import uri, request
from sqlalchemy import *
from collect import Collect
from cleaner import Cleaner
from adding import Install

print("creating tables...")
engine = create_engine(uri)

product.Base.metadata.create_all(engine)
category.Base.metadata.create_all(engine)
store.Base.metadata.create_all(engine)
print("tables created")
print("uploading data from api...")


products = Collect.collect(request)
table_prod = Cleaner.cleaner_prod(products)
table_cat = Cleaner.cleaner_cat(products)
table_store = Cleaner.cleaner_store(products)

print("upload successful")
print("adding data to tables...")
Install.install(table_prod, 'product', engine)
Install.install(table_cat, 'category', engine)
Install.install(table_store, 'store', engine)
print("database install with success")
