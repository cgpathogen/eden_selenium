import sqlite3
import os

class Database:
    db_path = os.path.join(os.path.dirname(__file__), "main.db")
    table_name = "products"

    @staticmethod
    def create_db():
        with sqlite3.connect(Database.db_path) as db:
            cur = db.cursor()
            cur.execute(f"""
            CREATE TABLE {Database.table_name}(
            product_id INTEGER NOT NULL PRIMARY KEY,
            product_name TEXT NOT NULL,
            product_price INTEGER NOT NULL
            )
            """)


    @staticmethod
    def update_data(name, price):
        with sqlite3.connect(Database.db_path) as db:
            cur = db.cursor()
            data = (name,price)
            cur.execute(f"""
            INSERT INTO {Database.table_name} (product_name, product_price)
            VALUES
            (?,?)
            """,data)
            db.commit()


    @staticmethod
    def select_item_data(id):
        with sqlite3.connect(Database.db_path) as db:
            cur = db.cursor()
            cur.execute(f"""
            SELECT product_name, product_price 
            FROM {Database.table_name} 
            WHERE product_id=?
            """,(id,))
            result = cur.fetchall()
            return result[0] if result else None