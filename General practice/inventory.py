# Inventory system using dictionary
inventory = {}

def display_inventory():
    if not inventory:
        print("Inventory is empty.")
    else:
        print("\nCurrent Inventory:")
        for item, details in inventory.items():
            print(f"{item}: Quantity = {details['quantity']}, Price = ₹{details['price']}")
    print()

def add_or_update_item():
    item = input("Enter item name: ").strip()
    quantity = int(input(f"Enter quantity for '{item}': "))
    price = float(input(f"Enter price for each '{item}': "))
    
    if item in inventory:
        inventory[item]['quantity'] += quantity
        inventory[item]['price'] = price 
        print(f"Updated '{item}' successfully.\n")
    else:
        inventory[item] = {'quantity': quantity, 'price': price}
        print(f"Added '{item}' to inventory.\n")

def sell_product():
    item = input("Enter item to sell: ").strip()
    quantity = int(input(f"Enter quantity to sell for '{item}': "))
    
    if item in inventory:
        if inventory[item]['quantity'] >= quantity:
            inventory[item]['quantity'] -= quantity
            total_price = quantity * inventory[item]['price']
            print(f"Sold {quantity} '{item}' for ₹{total_price:.2f}.\n")
            if inventory[item]['quantity'] == 0:
                print(f"'{item}' is now out of stock.\n")
        else:
            print(f"Insufficient quantity. Available: {inventory[item]['quantity']}\n")
    else:
        print(f"Item '{item}' not found in inventory.\n")

def inventory_menu():
    while True:
        print("===== Inventory Menu =====")
        print("1. Display Inventory")
        print("2. Add/Update Item")
        print("3. Sell Product")
        print("4. Quit")
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            display_inventory()
        elif choice == '2':
            add_or_update_item()
        elif choice == '3':
            sell_product()
        elif choice == '4':
            print("Exiting Inventory System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

inventory_menu()