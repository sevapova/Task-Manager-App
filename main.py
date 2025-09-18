from database import engine, metadata
from models import users, tasks
from sqlalchemy import insert, select, delete

metadata.create_all(engine)

def add_user():
    username = input("Foydalanuvchi username: ")
    fullname = input("Foydalanuvchi fullname: ")

    stmt = insert(users).values(username=username, fullname=fullname)
    with engine.begin() as conn:
        conn.execute(stmt)
    print("Foydalanuvchi qo'shildi.")

def list_users():
    stmt = select(users)
    with engine.connect() as conn:
        result = conn.execute(stmt)
        for row in result:
            print(row)

def get_user():
    user_id = int(input("Ko'rish uchun foydalanuvchi ID: "))
    stmt = select(users).where(users.c.id == user_id)
    with engine.connect() as conn:
        result = conn.execute(stmt).fetchone()
        if result:
            print(result)
        else:
            print("Bunday ID topilmadi.")

def delete_user():
    user_id = int(input("O'chirish uchun foydalanuvchi ID: "))
    stmt = delete(users).where(users.c.id == user_id)
    with engine.begin() as conn:
        result = conn.execute(stmt)
        if result.rowcount:
            print("Foydalanuvchi o'chirildi.")
        else:
            print("Bunday ID yo'q.")

def main():
    while True:
        print("\n--- MENYU ---")
        print("1. Foydalanuvchi qo'shish")
        print("2. Foydalanuvchilar ro'yxati")
        print("3. Foydalanuvchini ko'rish (ID bo'yicha)")
        print("4. Foydalanuvchini o'chirish")
        print("0. Chiqish")

        choice = input("Tanlov: ")

        if choice == "1":
            add_user()
        elif choice == "2":
            list_users()
        elif choice == "3":
            get_user()
        elif choice == "4":
            delete_user()
        elif choice == "0":
            print("Dastur tugadi. Bye bye ")
            break
        else:
            print("Noto'g'ri tanlov!")

if __name__ == "__main__":
    main()
