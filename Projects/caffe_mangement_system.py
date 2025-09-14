'''
The cafe management program which performs lot of operations according to the necesity. Majorly it maintains the file of the customer records and many more
'''

from datetime import datetime
class Order:
    def __init__(self, name, menu):
        self.name = name
        self.menu = menu
    def add_items(self):
        item_dict = {}
        items = [item for item in self.menu.keys()]
        cancel = False
        print("\nPress enter to add more\n0 to confirm order\n2 to cancel order\n")
        while not cancel:
            choice = input(f"{len(item_dict)+1}. ").lower().strip()
            if choice == '0':
                break
            elif choice == '2':
                cancel = True
            else:
                for item in items:
                    if item.lower() == choice:
                        item_dict.update({item: self.menu[item]})
                        break
                    # else:
                    #     print(f"Sorry ! {self.name}, this dish is unavailable as of now")
        return item_dict
    def remove_items(self, order):
        while len(order) > 0:
            choice = input("\nPress 1 to remove items and 2 to exit\n")
            if choice == '1':
                item_to_remove = input("\nEnter the item to remove\n").strip().lower()
                items = [item for item in order.keys()]
                for item in items:
                    if item.lower() == item_to_remove:
                        del order[item]
                        break
            elif choice == '2':
                break
            else:
                print("\nInvalid input !!!\n")
        else:
            print("\nOrder is empty nothing to remove\n")
        return order

        
        
menu = {

    "Margherita Pizza": 250,
    "Paneer Tikka": 180,
    "Veg Burger": 120,
    "French Fries": 90,
    "Cold Coffee": 80,
    "Chocolate Brownie": 110,
    "Masala Dosa": 140,
    "Pasta Alfredo": 200,
    "Chicken Biryani": 220,
    "Caesar Salad": 130,
    "Hot Chocolate": 100,
    "Samosa": 40,
    "Spring Rolls": 100,
    "Mojito": 90,
    "Grilled Sandwich": 110
}
customer_book = {}
order = {}
py_cafe = True
print('Welcome to PY_CAFE !!!\n')
for key, value in menu.items():
    print(f"{key} : {value}Rs")
    
new = True
while py_cafe:
    if new == True:
        name = input('\nEnter customer name:\n')
        print(f"Order and operations for {name}\n")

        cs1 = Order(name, menu)
    choice = int(input("\nPress 1 for add items\nPress 2 for remove items\nPress 3 confirm order\nPress 4 to exit\nPress 5 to show the customer book\n"))
    match choice:
        case 1:
            new = False
            order = cs1.add_items()
            print(f'\nOrder for {name}:\n')
            print()
            for key, value in order.items():
                print(f"{key} : {value}Rs")
            print(f"\nThe total bill for {name} is:  {sum(order.values())}\n")
        case 2:
            if order:
                updated_order = cs1.remove_items(order)
                for key, value in updated_order.items():
                    print(f"{key} : {value}Rs")
                print(f"The total bill for {name} is:  {sum(updated_order.values())}")
                order = updated_order
            else:
                print(f"No items in the order for {name}")
        case 3:
            print("\nFood preparation has begun. Please wait for a while...\n")
            print(f"Final bill for {name}: {sum(order.values())}Rs\n")
        case 4:
            now = datetime.now()
            customer_book.update({
                len(customer_book) + 1: {
                    "Name": name,
                    "Order": order,
                    "Date": now.strftime("%Y-%m-%d"),     
                    "Time": now.strftime("%H:%M:%S")     
                    }
                })

            print("\nThankyou so much... visit again !!\n")
            with open("customer_data.txt", 'a') as file:
                file.write(
                    f"\nOrder number: {len(customer_book)+1}\n"
                    f"Customer name: {name}\n"
                    f"Order:\n"
                )
                for item, price in order.items():
                    file.write(f"  {item}: {price} Rs\n")
                file.write(
                    f"Date: {now.strftime('%Y-%m-%d')}\n"
                    f"Time: {now.strftime('%H:%M:%S')}\n"
                    f"Total Bill: {sum(order.values())} Rs\n"
                    f"{'-'*40}\n"
                )

            new = True
        case 5:
            for key, value in customer_book.items():
                print(f"{key} -> {value}\n")
        case _:
            print("\nInvalid value entered\n")
    
