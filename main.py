from database import engine, metadata
from models import users, tasks

metadata.create_all(engine)


def main():
    pass

if __name__ == "__main__":
    main()
