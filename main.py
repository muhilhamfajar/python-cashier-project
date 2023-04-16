from userHandler import UserHandler

def main():
    userHandler = UserHandler()

    while True:
        print("\nMenu:")
        print("1. Add item")
        print("2. Update item name")
        print("3. Update item qty")
        print("4. Update item price")
        print("5. Delete item")
        print("6. Check order")
        print("7. Checkout")
        print("8. Reset transaction")
        print("99. Exit")

        choice = int(input("Masukkan pilihan Anda: "))

        if choice == 1:
            userHandler.menu_add()
        elif choice == 2:
            userHandler.menu_update_name()
        elif choice == 3:
            userHandler.menu_update_qty()
        elif choice == 4:
            userHandler.menu_update_price()
        elif choice == 5:
            userHandler.delete_item()
        elif choice == 6:
            userHandler.check_order()
        elif choice == 7:
            userHandler.check_out()
        elif choice == 8:
            userHandler.reset_transaction()
        elif choice == 99:
            print("Terima kasih, sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan angka antara 1-5.")

if __name__ == "__main__":
    main()