from sqlalchemy import create_engine, Table, Column, Integer, String, ForeignKey, MetaData

engine = create_engine("sqlite:///freebie_tracker.db")
metadata = MetaData()

# Assuming companies and devs tables already exist.

freebies = Table(
    "freebies",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("item_name", String, nullable=False),
    Column("value", Integer, nullable=False),
    Column("dev_id", Integer, ForeignKey("devs.id"), nullable=False),
    Column("company_id", Integer, ForeignKey("companies.id"), nullable=False),
)

metadata.create_all(engine)
print("Migration complete: freebies table created.")
