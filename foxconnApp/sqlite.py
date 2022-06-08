import sqlite3


def create():

    conn = sqlite3.connect('databaseF/equipment.db')

    cur = conn.cursor()

    cur.execute("CREATE TABLE equipment(name TEXT, price REAL, quantityLimit INTEGER)")

    cur.execute("INSERT INTO equipment (name, price, quantityLimit) VALUES ('pencil', 4.2, 10)")
    cur.execute("INSERT INTO equipment (name, price, quantityLimit) VALUES ('binder', 3.2, 10)")
    cur.execute("INSERT INTO equipment (name, price, quantityLimit) VALUES ('pen', 2.7, 10)")

    cur.close()

    conn.commit()


def read():
    conn = sqlite3.connect('databaseF/equipment.db')

    cur = conn.cursor()

    cur.execute("SELECT name, surname FROM orders")


    results = cur.fetchall()
    print(cur.description)
    print(results)



def tst():
    pass


read()