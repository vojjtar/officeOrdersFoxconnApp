import sqlite3
import string
import secrets

def createConnection():
    conn = None
    try:
        conn = sqlite3.connect('foxconnApp/databaseF/equipment.db')
    except Exception as e:
        print(e)

    return conn

def getPersonalId():
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(7))
    return password

def checkItem(finishData, item_quantity, itemLimit, itemPrice, itemName, totalPrice):
    if item_quantity > 0 and item_quantity <= itemLimit:
        totalPriceForItem = item_quantity * itemPrice
        finishData.append({"name": itemName, "quantity": item_quantity, "price": itemPrice, "totalPriceForItem": totalPriceForItem})

        return totalPriceForItem
    return 0