from models import product, category, store, save
from models.category import Category
from models.product import Product
from models.save import Save
from models import Base
from config import uri
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from collector import Collector
from cleaner import Cleaner
from installer import Installer

class App:

    def create_db() :
    
        ''' 
        Create database, collect data and insert them 
        '''

        # create tables in mysql using models

        print("creating tables...")
        engine = create_engine(uri)
        Base.metadata.create_all(engine)
        print("tables created")
    
        # collect data from api and prepare them to insert into tables

        print("uploading data from api...")
        this = Collector()
        products = Collector.collect(this)
        table = Cleaner.cleaner(products)
        print("upload successful")

        # insert data in tables

        print("adding data to tables...")
        Installer.install(table, engine)
        print("database install with success")

    def view_cat() -> dict: 

        ''' 
        Return a dictonnary of all categories present in the table 
        '''

        engine = create_engine(uri)
        Session = sessionmaker(bind=engine)
        session = Session()
        cat = {}
        i = 1
        for row in session.query(Category).all():
            cat[str(i)] = row.name
            i += 1
        cat['0'] = 'retour'    
        return cat
    
    def view_prod(entry: int) -> dict:

        ''' 
        Return a dictonnary of all products in a category
        '''

        engine = create_engine(uri)
        Session = sessionmaker(bind=engine)
        session = Session()
        i = 1
        prod = {}
        for row in session.query(Product).select_from(Category)\
            .join(Category.products)\
            .filter(Category.code == entry):
            prod[str(i)] = row.name
            i += 1
        prod['0'] = 'retour'
        return prod

    def view_save() -> list:

        ''' 
        Return a list of all substitutes saved
        '''

        save = []
        engine = create_engine(uri)
        Session = sessionmaker(bind=engine)
        session = Session()
        for row in session.query(Save).all():
            save.append(row.name)
        return save

    def search_alt(prod_name : str) -> dict:
        engine = create_engine(uri)
        Session = sessionmaker(bind=engine)
        session = Session()
        alt_prod = {}
        for row in session.query(Category).select_from(Product)\
            .join(Product.categories)\
            .filter(Product.name == prod_name):
            for row_2 in session.query(Product).select_from(Category)\
            .join(Category.products)\
            .filter(Category.name == row.name):
                alt_prod[row_2.name] = row_2.score
        del alt_prod[prod_name]
        return alt_prod

    def relevance(alt: dict) -> str :

        ''' 
        Search a relevant product to substitute a product given 
        '''

        s = None
        for k, v in alt.items():
            if v is None :
                pass
            elif s is None:
                s = v
                sub = k
            elif s > v:
                s = v 
                sub = k
        return sub

    def insert_sub(name: str) -> str:

        ''' 
        Insert a product in the table 'save'
        '''

        engine = create_engine(uri)
        Session = sessionmaker(bind=engine)
        session = Session()
        suspect = session.query(Save).filter(Save.name == name).one_or_none()
        if suspect is None :
            add = Save(name=name)
            session.add(add)
            session.commit()
            feedback = 'Substitut enregistré'

        else :
            feedback = 'Substitut déjà présent dans votre liste'

        return feedback    