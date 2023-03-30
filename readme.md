# Python Project

Create a simple project using Python language that is connected to SQLite for the Pacmann final project about supermarket.

### A. Background Problems
Andi is an owner of a large supermarket in one of the cities in Indonesia. Andi has a plan to improve the business process, which is to create a self-service cashier system in his supermarket with the hope of:
-   Customers can directly input the items they purchase, the quantity of each item, the price of each item, and other features.
-   Customers who are not located in the city can also buy items from the supermarket.

After conducting research, Andi found out that he has a problem, which is that he needs a programmer to create features so that the self-service cashier system in his supermarket can run smoothly.

### B. Objectives

Program Objectives:
-   Users can place an order for items.
-   Users can modify their order.
-   Users can check their order.
-   Users can checkout and pay for their order.
-   All orders are saved in a database.

Learning Objectives:
-   Able to code using Python programming language
-   Create the features that have been mentioned in the requirements
-   Modular code
-   Clean code (PEP8)
-   Docstrings documentation in the created functions
-   Include try-except error handling in branching for easy error tracking (defense programming)
-   Connect to SQLite database.

### C. Flowchart
link gambar

### D. Penjelasan Function
Here is the explanation of each function:

1.  `__init__`: This function is used to initialize a transaction object with empty attributes and create a connection to the SQLite database 'transactions.db'. The `create_table` function is called to create the transaction table if it does not already exist.
    
2.  `add_item`: This function is used to add one or more items to the transaction. It takes a tuple containing the item name, item quantity, and item price for each item.
    
3.  `update_item_name`: This function is used to change the name of an item in the transaction. It takes the current item name and the new item name.
    
4.  `update_item_qty`: This function is used to change the quantity of an item in the transaction. It takes the item name and the new item quantity.
    
5.  `update_item_price`: This function is used to change the price of an item in the transaction. It takes the item name and the new item price.
    
6.  `delete_item`: This function is used to remove an item from the transaction. It takes the name of the item to be deleted.
    
7.  `check_order`: This function is used to check if there are any input errors in the transaction and print the transaction details in a table format.
    
8.  `create_table`: This function is used to create the transaction table if it does not already exist.
    
9.  `insert_to_table`: This function is used to insert transaction data into the transaction table.
    
10.  `check_out`: This function is used to calculate the total price of the transaction, apply discounts if applicable, and save the transaction data to the SQLite database.
    
11.  `reset_transaction`: This function is used to reset the transaction by clearing all the items.

### E. Test Case
Before running test cases, I have created unit tests to ensure that each small part of the code program runs as expected in isolation.
Here is the test case
1. Test 1 (add item)
2. Test 2 (modify item)
3. Test 3 (delete item)
4. Test 4 (reset transaction)
5. Test 5 (checkout)
   
### F. Saran Perbaikan
### Conclusion