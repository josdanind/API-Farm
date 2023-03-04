#SQLAlchemy
from sqlalchemy import Table, Column, Integer, String, Float
from sqlalchemy import MetaData

from config import metadata

# metadata = MetaData()

movies = Table(
    "movies",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String),
    Column("overview", String),
    Column("year", String),
    Column("rating", Float),
    Column("category", String),
)

