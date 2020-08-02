from sqlalchemy.orm import sessionmaker
from models.product import Product
from models.category import Category
from models.store import Store


class Installer:
    def install(self, data: dict, engine: object):
        """Insert data in related table and create associations between data."""
        Session = sessionmaker(bind=engine)
        session = Session()
        for key, element in data.items():
            # checking if element exist
            if element.get("code") is not None:
                # checking if element is already in table
                clue = element.get("code")
                suspect = (
                    session.query(Product)
                    .filter(Product.code == clue)
                    .one_or_none()
                )
                if suspect is None:
                    # insert data in table
                    code = clue
                    product = element.get("product")
                    add_prod = Product(
                        code=code,
                        name=product.get("name"),
                        ingredients=product.get("ingredients"),
                        brand=product.get("brands"),
                        labels=product.get("labels"),
                        score=product.get("score"),
                    )
                    session.add(add_prod)
                    session.commit()

                stores = element.get("stores")
                for key_2, element_2 in stores.items():
                    # checking if element exist
                    if element_2 is not None:
                        # checking if element is already in table
                        clue = element_2
                        suspect = (
                            session.query(Store)
                            .filter(Store.name == clue)
                            .one_or_none()
                        )
                        if suspect is None:
                            # insert data in table
                            add_store = Store(name=clue)
                            session.add(add_store)
                            session.commit()
                        # insert association between a product and a store
                        store = (
                            session.query(Store)
                            .filter(Store.name == element_2)
                            .first()
                        )
                        prod = (
                            session.query(Product)
                            .filter(Product.code == element.get("code"))
                            .first()
                        )
                        store.products.append(prod)
                        session.commit()

                categories = element.get("categories")
                for key_2, element_2 in categories.items():
                    # checking if element exist
                    if element_2 is not None:
                        # checking if element is already in table
                        clue = element_2
                        suspect = (
                            session.query(Category)
                            .filter(Category.name == clue)
                            .one_or_none()
                        )
                        if suspect is None:
                            # insert data in table
                            add = Category(name=clue)
                            session.add(add)
                            session.commit()
                        # insert association between a product and a category
                        cat = (
                            session.query(Category)
                            .filter(Category.name == clue)
                            .first()
                        )
                        prod = (
                            session.query(Product)
                            .filter(Product.code == element.get("code"))
                            .first()
                        )
                        cat.products.append(prod)
                        session.commit()
