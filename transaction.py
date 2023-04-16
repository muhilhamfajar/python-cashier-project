import sqlite3

class Transaction:
    """Class to process transactions."""

    def __init__(self):
        """Initialize an empty transaction."""
        self.items = {}
        self.conn = sqlite3.connect('transactions.db')
        self.create_table()

    def add_items(self, *items):
        """Add one or more items to the transaction.

        Args:
            items (tuple): A tuple containing item name, item quantity, and item price for each item.
        """
        for item_data in items:
            try:
                name, qty, price = item_data
                if name in self.items:
                    self.items[name]['quantity'] += qty
                    self.items[name]['price'] = price
                else:
                    self.items[name] = {'quantity': qty, 'price': price}
            except ValueError:
                print("Invalid item data. Please provide a tuple with the item name, quantity, and price.")

    def update_item_name(self, name, new_name):
        """Update the name of an item.

        Args:
            name (str): The current name of the item.
            new_name (str): The new name of the item.
        """
        try:
            if name in self.items:
                self.items[new_name] = self.items.pop(name)
                return True
            else:
                print(f"Item '{name}' not found.")
        except KeyError:
            print(f"Unable to update item name '{name}'.")

    def update_item_qty(self, name, new_qty):
        """Update the quantity of an item.

        Args:
            name (str): The name of the item.
            new_qty (int): The new quantity of the item.
        """
        try:
            if name in self.items:
                self.items[name]['quantity'] = new_qty
                return True
            else:
                print(f"Item '{name}' not found.")
        except KeyError:
            print(f"Unable to update item quantity for '{name}'.")

    def update_item_price(self, name, new_price):
        """Update the price of an item.

        Args:
            name (str): The name of the item.
            new_price (float): The new price of the item.
        """
        try:
            if name in self.items:
                self.items[name]['price'] = new_price
                return True
            else:
                print(f"Item '{name}' not found.")
        except KeyError:
            print(f"Unable to update item price for '{name}'.")

    def delete_item(self, name):
        """Delete an item from the transaction.

        Args:
            name (str): The name of the item to delete.
        """
        try:
            if name in self.items:
                del self.items[name]
                return True
            else:
                print(f"Item '{name}' not found.")
        except KeyError:
            print(f"Unable to delete item '{name}'.")

    def check_order(self):
        """Check if there are any input errors in the transaction and print the transaction details in a table."""

        if not self.items:
            print("Terdapat kesalahan input data. Tidak ada item dalam transaksi.")
            return

        error = False
        for item_name, item_data in self.items.items():
            if not isinstance(item_name, str) or not item_name:
                print(f"Terdapat kesalahan input data. Nama item tidak valid: '{item_name}'.")
                error = True

            quantity = item_data.get('quantity')
            price = item_data.get('price')

            if not isinstance(quantity, int) or quantity <= 0:
                print(f"Terdapat kesalahan input data. Kuantitas tidak valid untuk item '{item_name}': {quantity}.")
                error = True

            if not isinstance(price, (int, float)) or price < 0:
                print(f"Terdapat kesalahan input data. Harga tidak valid untuk item '{item_name}': {price}.")
                error = True

        if not error:
            print("\nDaftar Pemesanan:")
            print("----------------------------------------------------")
            print("| Nama Barang  | Kuantitas | Harga Satuan | Total  |")
            print("----------------------------------------------------")

            for item_name, item_data in self.items.items():
                quantity = item_data['quantity']
                price = item_data['price']
                total = quantity * price
                print(f"| {item_name:<12} | {quantity:^9} | {price:^12} | {total:^6} |")

            print("----------------------------------------------------")

    def create_table(self):
        """Create the transaction table if it doesn't exist."""
        try:
            cursor = self.conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
                                no_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nama_item TEXT NOT NULL,
                                jumlah_item INTEGER NOT NULL,
                                harga REAL NOT NULL,
                                total_harga REAL NOT NULL,
                                diskon REAL NOT NULL,
                                harga_diskon REAL NOT NULL
                            )''')
            self.conn.commit()
        except sqlite3.Error as e:
            print("Error while creating the transactions table:", e)

    def insert_to_table(self, source_data):
        """Insert transaction data into the transaction table."""

        try:
            cursor = self.conn.cursor()
            cursor.execute('''INSERT INTO transactions (nama_item, jumlah_item, harga, total_harga, diskon, harga_diskon)
                              VALUES (?, ?, ?, ?, ?, ?)''', source_data)
            self.conn.commit()
        except sqlite3.Error as e:
            print("Error while inserting data into the transactions table:", e)

    def check_out(self):
        """Calculate the total price of the transaction and apply discounts, then insert the transaction data into the SQLite database."""

        if not self.items:
            print("Tidak ada item dalam transaksi. Harap tambahkan item terlebih dahulu.")
            return

        try:
            for item_name, item_data in self.items.items():
                quantity = item_data['quantity']
                price = item_data['price']
                item_total = quantity * price

                # Apply discounts based on the total price per item
                if item_total > 500000:
                    discount_percent = 0.07
                elif item_total > 300000:
                    discount_percent = 0.06
                elif item_total > 200000:
                    discount_percent = 0.05
                else:
                    discount_percent = 0

                discounted_total = item_total * (1 - discount_percent)
                discount = item_total - discounted_total

                # Insert transaction data into the SQLite database
                source_data = (item_name, quantity, price, item_total, discount, discounted_total)
                self.insert_to_table(source_data)

            self.reset_transaction()
            print("Transaksi berhasil disimpan ke dalam database.")

        except Exception as e:
            print("Terjadi kesalahan saat melakukan check_out:", e)

        self.conn.close()

    def reset_transaction(self):
        """Reset the transaction by clearing all items."""
        self.items.clear()
        print('Semua item berhasil didelete')