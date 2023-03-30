import unittest
from transaction import Transaction

class TestTransaction(unittest.TestCase):

    def setUp(self):
        self.transaction = Transaction()

    def test_add_item(self):
        self.transaction.add_item(('Laptop', 1, 15000000))
        self.assertEqual(self.transaction.items, {'Laptop': {'quantity': 1, 'price': 15000000}})

    def test_update_item_name(self):
        self.transaction.add_item(('Laptop', 1, 15000000))
        self.transaction.update_item_name('Laptop', 'Notebook')
        self.assertEqual(self.transaction.items, {'Notebook': {'quantity': 1, 'price': 15000000}})

    def test_update_item_qty(self):
        self.transaction.add_item(('Laptop', 1, 15000000))
        self.transaction.update_item_qty('Laptop', 2)
        self.assertEqual(self.transaction.items['Laptop']['quantity'], 2)

    def test_update_item_price(self):
        self.transaction.add_item(('Laptop', 1, 15000000))
        self.transaction.update_item_price('Laptop', 16000000)
        self.assertEqual(self.transaction.items['Laptop']['price'], 16000000)

    def test_delete_item(self):
        self.transaction.add_item(('Laptop', 1, 15000000))
        self.transaction.delete_item('Laptop')
        self.assertEqual(self.transaction.items, {})

    def test_reset_transaction(self):
        self.transaction.add_item(('Laptop', 1, 15000000))
        self.transaction.reset_transaction()
        self.assertEqual(self.transaction.items, {})

    def tearDown(self):
        self.transaction.conn.close()

if __name__ == '__main__':
    unittest.main()
