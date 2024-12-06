import sqlite3


def initiate_db():
    cursor.execute("""                          
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    """)


def get_all_products():
    cursor.execute("SELECT * FROM Products")
    users = cursor.fetchall()
    return users


conection = sqlite3.connect('product_base.db')
cursor = conection.cursor()

if __name__ == '__main__':
    initiate_db()

    for i in range(4):
        cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
                       (f'Продукт {i + 1}', f'Описание {i + 1}', (i + 1) * 100))

    conection.commit()
    conection.close()
