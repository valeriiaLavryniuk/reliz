import pprint
import sqlite3

def create_table():
    conn = sqlite3.connect("data_base.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY,
            name TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS item (
            id INTEGER PRIMARY KEY,
            name TEXT,
            desc TEXT,
            img TEXT,
            price INTEGER,
            category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES categories(id)
        )
    ''')
    conn.commit()
    conn.close()

def fill_item(path_to_db):
    n = int(input("Введіть кількість речей: "))
    conn = sqlite3.connect(path_to_db)
    cur = conn.cursor()
    for i in range(n):
        name = input(f"Введіть назву: ")
        desc = input(f"Введіть опис: ")
        img = input(f"Введіть фото: ")
        price = int(input(f"Введіть ціну: "))
        cur.execute('''INSERT INTO item (name, desc, img, price) VALUES (?,?,?,?)''', [name, desc, img, price])
        conn.commit()
    conn.close()

def fill_category(path_to_db):
    n = int(input("Введіть кількість категорій: "))
    conn = sqlite3.connect(path_to_db)
    cur = conn.cursor()
    for i in range(n):
        name = input(f"Категорія під номером {i}: ")
        cur.execute('''INSERT INTO categories (name) VALUES (?)''', [name])
        conn.commit()
    conn.close()

create_table()
#fill_category("data_base.db")
fill_item("data_base.db")

def print_items(path_to_db):
    conn = sqlite3.connect(path_to_db)
    cur = conn.cursor()
    i = 1
    cur.execute("SELECT * FROM item")
    items = cur.fetchall()
    pprint.pprint(items)
    for item in items:
        print(item)

    conn.close()
    return items

print_items("data_base.db")
