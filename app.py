from models import product, category, store
from models.category import Category
from models import Base
from config import uri
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from collector import Collector
from cleaner import Cleaner
from adding import Installer

class App:

    def create_db() :

        ''' create tables in mysql using models '''

        print("creating tables...")
        engine = create_engine(uri)
        Base.metadata.create_all(engine)
        print("tables created")
    
        ''' collect data from api and prepare them to insert into tables '''

        print("uploading data from api...")
        this = Collector()
        products = Collector.collect(this)
        table = Cleaner.cleaner(products)
        print("upload successful")

        ''' insert data in tables '''

        print("adding data to tables...")
        Installer.install(table, engine)
        print("database install with success")

    def view_cat():
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
    
    def view_prod(cat):
        engine = create_engine(uri)
        Session = sessionmaker(bind=engine)
        session = Session()
        prod = {}
        '''  
            1 /     Mettre les tables associatives en place
            2 /     Recherche dans la table associative avec filter() les codes des produits
            3 /     Recherche dans la table product avec filtre() les produits
        '''
        return prod

    def view_save():
        ''' code pour chercher les substituts enregistrés et return dict'''

        pass

    def search_alt(prod):
        ''' code pour trouver un substitut et afficher ses infos '''

        pass
