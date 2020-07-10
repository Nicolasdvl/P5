from sqlalchemy import Table, ForeignKey, Column, Integer, String, BigInteger
from sqlalchemy.orm import relationship
from models import Base
from models import product


prod_cat = Table('prod_cat', Base.metadata,
    Column('prod_id', BigInteger, ForeignKey('product.code')),
    Column('cat_id', Integer, ForeignKey('category.code'))
    )

class Category (Base):
    __tablename__ = "category"

    code = Column(Integer, autoincrement=True, primary_key =True)
    name = Column(String(120), nullable =False, unique =True)
    products = relationship(
        "Product",
        secondary=prod_cat,
        back_populates="categories"
    )