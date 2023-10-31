"""
This program allows customers to place orders from a food truck menu. The menu is organized into categories such as snacks, meals, drinks, and desserts. Customers can select a category and then choose an item from that category. They can also specify the quantity of each item they want to order. The program keeps track of the customer's order and presents a summary at the end. 
"""
# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list.
order_list = []

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings.
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1

            # Get customer's menu item number
            menu_selection = input("Please enter the number of your menu selection: ")

            # Check if the customer's input is a number
            if not menu_selection.isdigit():
                print("Error: Please enter a valid number.")
            else:
                menu_selection = int(menu_selection)
                if menu_selection in menu_items.keys():
                    item_name = menu_items[menu_selection]["Item name"]
                    price = menu_items[menu_selection]["Price"]

                    # Ask the customer for the quantity of the menu item
                    quantity = input(f"How many {item_name} would you like to order? (Default is 1 if invalid input): ")
                    if not quantity.isdigit():
                        quantity = 1
                    else:
                        quantity = int(quantity)

                    order_list.append({
                        "Item name": item_name,
                        "Price": price,
                        "Quantity": quantity
                    })
                else:
                    print("Error: This item is not on the menu.")
        else:
            print(f"{menu_category} was not a menu option.")
    else:
        print("You didn't select a number.")

    while True:
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ").lower()
        match keep_ordering:
            case 'y':
                break
            case 'n':
                place_order = False
                print("Thank you for your order.")
                break
            case _:
                print("Invalid input. Please enter 'y' or 'n'.")

# Print out the customer's order
print("\nOrder Receipt")
print("Item name".ljust(25) + "| Price".ljust(10) + "| Quantity".ljust(10))
print("-" * 50)
for order in order_list:
    item_name = order["Item name"]
    price = order["Price"]
    quantity = order["Quantity"]
    print(item_name.ljust(25) + f"| ${price:.2f}".ljust(10) + f"| {quantity}".ljust(10))
    
total_price = sum([order["Price"] * order["Quantity"] for order in order_list])
print("\nTotal Price:", f"${total_price:.2f}")
