import ipdb
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Dev, Freebie

engine = create_engine("sqlite:///freebie_tracker.db")
Session = sessionmaker(bind=engine)
session = Session()

ipdb.set_trace()
