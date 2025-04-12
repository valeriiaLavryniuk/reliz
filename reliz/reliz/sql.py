import sqlite3

def select(sql, param = None):
    conn = sqlite3.Connection("data_base.db")
    cur = conn.cursor()
    if param:
        cur.execute(sql, param)
    else:
        cur.execute(sql)
    data = cur.fetchall()
    conn.close()
    return data

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
        id = input(f"Введіть річ під номером {i}: ")
        name = input(f"Введіть назву: ")
        desc = input(f"Введіть опис: ")
        price = input(f"Введіть ціну: ")

        cur.execute('''INSERT INTO questions (id, name, desc, price) VALUES (?,?,?,?)''', [id, name, desc, price])
        conn.commit()
    conn.close()


def fill_category(path_to_db):
    n = int(input("Введіть кількість категорій: "))
    conn = sqlite3.connect(path_to_db)
    cur = conn.cursor()

    for i in range(n):
        name = input(f"Категорія під номером {i}: ")
        cur.execute('''INSERT INTO category (name) VALUES (?)''', [name])
        conn.commit()
    conn.close()


#def fill_content(path_to_db):
    #n = int(input("Введіть кількість id: "))
    #conn = sqlite3.connect(path_to_db)
    #cur = conn.cursor()
    #for i in range(n):
     #   quiz_id = input(f"Id категорії під номером {i+1}: ")
      #  question_id = input(f"Id речі під номером {i+1}: ")
     #   cur.execute('''INSERT INTO quiz_content (categories_id, item_id) VALUES (?,?)''', [categories_id, item_id])
      #  conn.commit()
   # conn.close()

create_table("data_base.db")
fill_category("data_base.db")
fill_item("data_base.db")
# fill_content("data_base.db")

def print_questions(path_to_db):
    conn = sqlite3.connect(path_to_db)
    cur = conn.cursor()
    i = 1
    for i in range(3,13):
        cur.execute("SELECT * FROM questions WHERE id == ?", [i])
        data = cur.fetchall()
        print(data)
        conn.commit()
    conn.close()

print_questions("data_base.db")
