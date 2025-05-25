from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Dev, Freebie

engine = create_engine("sqlite:///freebie_tracker.db")
Session = sessionmaker(bind=engine)
session = Session()

# Create tables if not already created
Base.metadata.create_all(engine)

# Seed companies
company1 = Company(name="TechCorp", founding_year=1985)
company2 = Company(name="DevWorks", founding_year=1995)

# Seed devs
dev1 = Dev(name="Alice")
dev2 = Dev(name="Bob")

session.add_all([company1, company2, dev1, dev2])
session.commit()

# Seed freebies
freebie1 = company1.give_freebie(dev1, "T-Shirt", 25)
freebie2 = company2.give_freebie(dev2, "Sticker Pack", 5)

session.add_all([freebie1, freebie2])
session.commit()

print("Seed data created successfully.")
