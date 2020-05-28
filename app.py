from models import data, stores, categories
from config import uri
from sqlalchemy import *

engine = create_engine(uri)

data.Base.metadata.create_all(engine)
categories.Base.metadata.create_all(engine)
stores.Base.metadata.create_all(engine)