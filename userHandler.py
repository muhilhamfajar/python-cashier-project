from transaction import Transaction

class UserHandler:
    """" Class to handler user transaction """

    def __init__(self):
        """Initialize an empty transaction."""
        self.transaction = Transaction()

    def menu_add(self):
        """ Handler add menu """

        name = input("Masukkan item yang ingin ditambahkan: ")
        quantity = int(input("Masukkan jumlah item: "))
        price = int(input("Masukkan harga per item: "))
        
        self.transaction.add_items([name, quantity, price])
        print('Item berhasil ditambahkan')

    def menu_update_name(self):
        """ Handler update menu name """

        name = input("Masukkan item yang ingin diupdate: ")
        new_name = input("Masukkan nama item baru: ")
        
        success = self.transaction.update_item_name(name, new_name)
        if success:
            print(f"Item {name} berhasil diupdate menjadi {new_name}")

    def menu_update_qty(self):
        """ Handler update menu quantity """

        name = input("Masukkan item yang ingin diupdate: ")
        new_qty = int(input("Masukkan jumlah item baru: "))
        
        success = self.transaction.update_item_qty(name, new_qty)
        if success:
            print(f"Quantity item {name} berhasil diupdate menjadi {new_qty}")

    def menu_update_price(self):
        """ Handler update price item """

        name = input("Masukkan item yang ingin diupdate: ")
        new_price = int(input("Masukkan harga item baru: "))
        
        success = self.transaction.update_item_price(name, new_price)
        if success:
            print(f"Harga item {name} berhasil diupdate menjadi {new_price}")

    def delete_item(self):
        """ Handler delete item """

        name = input("Masukkan item yang ingin didelete: ")
        
        success = self.transaction.delete_item(name)
        if success:
            print(f"Item {name} berhasil didelete")

    def check_order(self):
        """ Handler check order """

        return self.transaction.check_order()
    
    def check_out(self):
        """ Handler checkout """

        return self.transaction.check_out()
    
    def reset_transaction(self):
        """ Handler reset transaction """

        return self.transaction.reset_transaction()
