from sqlalchemy import create_engine, URL, MetaData
from config import settings

url = URL.create(
    drivername="postgresql+psycopg2",
    username=settings.USER,
    password=settings.PASSWORD,
    host=settings.HOST,
    port=settings.PORT,
    database=settings.DBNAME
)

engine = create_engine(url) # "dialect+driver://username:password@host:port/database"
metadata = MetaData()

