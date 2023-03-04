# Standard Library
from os import environ

# Databases
from databases import Database

# SQLAlchemy
import sqlalchemy

# Environment varibles
DB_URL = environ["DB_URL"]

engine = sqlalchemy.create_engine(DB_URL, echo=True)
metadata = sqlalchemy.MetaData()

database = Database(DB_URL)
