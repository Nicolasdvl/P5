from sqlalchemy import Column, String, BigInteger
from models import Base


class Save(Base):
    __tablename__ = "save"

    code = Column(BigInteger, primary_key=True)
    prod_name = Column(String(120), nullable=False, unique=True)
    sub_name = Column(String(120), nullable=False, unique=True)
