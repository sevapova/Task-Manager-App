import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    HOST = os.getenv("HOST")
    PORT = os.getenv("PORT")
    USER = os.getenv("USER")
    PASSWORD = os.getenv("PASSWORD")
    DBNAME = os.getenv("DBNAME")

settings = Settings()
