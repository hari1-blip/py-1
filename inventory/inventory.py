import sqlite3



def init_db():
    conn = sqlite3.connect('inventory.db')

    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS inventory(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL,
               quantity TEXT NOT NULL,
               price REAL NOT NULL
                      
               )    
''')
    conn.commit()
    conn.close()


def add_item():
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    name = input('enter the name:')
    quantity = input('enter the quantity:')
    price = input('enter the price of the product:')

    cursor.execute('INSERT INTO inventory (name, quantity,price) VALUES (?,?,?)',(name,quantity,price))

    conn.commit()
    conn.close()

    print('item added to the inventory succesfully!')

def view_items():
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM inventory")
    items = cursor.fetchall()
    if items:
        for item in items:
            print(f'ID:{item[0]} ,NAME:{item[1]},Quantity:{item[2]},Price:{item[3]:.2f}')

    else :
        print('No items in the inventory!')
    
    conn.close()

def delete_items():
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()

    item_id = int(input('enter the item id to delete from the inventory:'))

    cursor.execute("SELECT * FROM inventory WHERE id = ?",(item_id,))
    item = cursor.fetchone()
    if item:
        cursor.execute("DELETE FROM inventory WHERE id = ?",(item_id,))
        conn.commit()
        print('item deleted succesfully!')
    else:
        print('item not found!')
    conn.close()

def display_menu():
    print("choose any options")
    print('''
1.add item
2.view item
3.delete item
4.exit
''')
        
def main():
    while True:
        init_db()
        display_menu()

        choice = input('enter any choice:')

        if choice == '1':
            add_item()

        elif choice == '2':
            view_items()

        elif choice == '3':
            delete_items()

        elif choice == '4':
            break


if __name__ == "__main__":
    main()