from models.category import Category
from models.product import Product
from models.save import Save
from models import Base
from config import URI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from collector import Collector
from cleaner import Cleaner
from installer import Installer


class App:
    def __init__(self):
        self.engine = create_engine(URI)

    def create_db(self):
        """Create database, collect data and insert them."""
        print("creating tables...")
        Base.metadata.create_all(self.engine)
        print("tables created")
        print("uploading data from api...")
        collector = Collector()
        data = collector.collect()
        cleaner = Cleaner()
        data_cleaned = cleaner.cleaner(data)
        print("upload successful")
        print("adding data to tables...")
        installer = Installer()
        installer.install(data_cleaned, self.engine)
        print("database install with success")

    def view_cat(self) -> dict:
        """Return a dictonnary of all categories present in the table."""
        Session = sessionmaker(bind=self.engine)
        session = Session()
        cat = {}
        i = 1
        for row in session.query(Category).all():
            cat[str(i)] = row.name
            i += 1
        cat["0"] = "retour"
        return cat

    def view_prod(self, entry: int) -> dict:
        """Return a dictonnary of all products in a category."""
        Session = sessionmaker(bind=self.engine)
        session = Session()
        i = 1
        prod = {}
        for row in (
            session.query(Product)
            .select_from(Category)
            .join(Category.products)
            .filter(Category.code == entry)
        ):
            prod[str(i)] = row.name
            i += 1
        prod["0"] = "retour"
        return prod

    def view_save(self) -> list:
        """Return a list of all substitutes saved."""
        save = []
        Session = sessionmaker(bind=self.engine)
        session = Session()
        for row in session.query(Save).all():
            save.append(row.name)
        return save

    def search_alt(self, prod_name: str) -> dict:
        """Return a dict of products ordered by nutri-score."""
        Session = sessionmaker(bind=self.engine)
        session = Session()
        alt_prod = {}
        for row in (
            session.query(Category)
            .select_from(Product)
            .join(Product.categories)
            .filter(Product.name == prod_name)
        ):
            for row_2 in (
                session.query(Product)
                .select_from(Category)
                .join(Category.products)
                .filter(Category.name == row.name)
            ):
                alt_prod[row_2.name] = row_2.score
        del alt_prod[prod_name]
        return alt_prod

    def relevance(self, alt: dict) -> str:
        """Search a relevant product to substitute a product given."""
        substitute_score = None
        for product_name, product_score in alt.items():
            if product_score is None:
                pass
            elif substitute_score is None:
                substitute_score = product_score
                substitute_name = product_name
            elif substitute_score > product_score:
                substitute_score = product_score
                substitute_name = product_name
        return substitute_name

    def insert_sub(self, name: str) -> str:
        """Insert a product in the table 'save'."""
        Session = sessionmaker(bind=self.engine)
        session = Session()
        suspect = session.query(Save).filter(Save.name == name).one_or_none()
        if suspect is None:
            add = Save(name=name)
            session.add(add)
            session.commit()
            feedback = "Substitut enregistré"
        else:
            feedback = "Substitut déjà présent dans votre liste"
        return feedback
