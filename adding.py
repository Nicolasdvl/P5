from sqlalchemy.orm import sessionmaker
from models.product import Product
from models.category import Category
from models.store import Store

class Installer():

    def install(data, table_name, engine):
        Session = sessionmaker(bind=engine)
        session = Session()

        if table_name == 'product' :
            for pos, element in enumerate(data):
                clue = str(data[pos][0])
                suspect = session.query(Product).filter(Product.code == clue).one_or_none()
                if suspect is None :
                    add = Product(code=data[pos][0], name=data[pos][1], ingredients=data[pos][2], brand=data[pos][3], labels=data[pos][4], score=data[pos][5])
                    session.add(add)
                    session.commit()

        elif table_name == 'category' :
            for pos, element in enumerate(data):
                clue = str(data[pos])
                suspect = session.query(Category).filter(Category.name == clue).one_or_none()
                if suspect is None :
                    add = Category(name=data[pos])
                    session.add(add)
                    session.commit()

        elif table_name == 'store' :
            for pos, element in enumerate(data):
                clue = str(data[pos])
                suspect = session.query(Store).filter(Store.name == clue).one_or_none()
                if suspect is None :
                    add = Store(name=data[pos])
                    session.add(add)
                    session.commit()
