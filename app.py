from models import product, store, category
from config import uri
from sqlalchemy import create_engine
from collector import Collector
from cleaner import Cleaner
from adding import Installer


def main() :

    ''' create tables in mysql using models '''

    print("creating tables...")
    engine = create_engine(uri)
    product.Base.metadata.create_all(engine)
    category.Base.metadata.create_all(engine)
    store.Base.metadata.create_all(engine)
    print("tables created")
   
    ''' collect data from api and prepare them to insert into tables '''

    print("uploading data from api...")
    this = Collector()
    products = Collector.collect(this)
    table_prod = Cleaner.cleaner_prod(products)
    table_cat = Cleaner.cleaner_cat(products)
    table_store = Cleaner.cleaner_store(products)
    print("upload successful")

    ''' insert data in tables '''

    print("adding data to tables...")
    Installer.install(table_prod, 'product', engine)
    Installer.install(table_cat, 'category', engine)
    Installer.install(table_store, 'store', engine)
    print("database install with success")


if __name__ == "__main__" :
    main()