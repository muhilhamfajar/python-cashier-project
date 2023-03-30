from transaction import Transaction

transaction1 = Transaction()
transaction1.add_item(['Ayam Goreng', 2, 20000], ['Pasta Gigi', 3, 1500])
transaction1.delete_item('Pasta Gigi')
transaction1.check_order()
transaction1.check_out()