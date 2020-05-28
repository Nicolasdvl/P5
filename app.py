from models import data
from sqlalchemy import *

engine = create_engine('mysql+pymysql://root:@localhost/p5')

if not engine.dialect.has_table(engine, 'data'):
    data.Base.metadata.create_all(engine)

else:
    pass