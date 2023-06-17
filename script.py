from transaction import Transaction
import sys

MENU = {
    '1': 'Add Item',
    '2': 'Update Item Name',
    '3': 'Update Item Price',
    '4': 'Update Item Quantity',
    '5': 'Delete an Item',
    '6': 'Delete All Items',
    '7': 'Show Cart',
    '8': 'Calculate Total',
    '0': 'Exit'
}

def display_menu():
    """ Display the cashier program menu. """
    print("===== Cashier Program Menu =====")
    
    for key, value in MENU.items():
        print(f"{key}. {value}")

def input_item_name(prompt_text):
    """Prompt the user to input an item name.

    Parameters:
    -----------
    prompt_text : str
        The prompt text for input.

    Returns:
    -----------
    str: 
        The item name entered by the user if the input is not empty.
    """
    item_name = input(prompt_text)

    if input_not_empty(item_name):
        return item_name.capitalize()
    
    else:
        print("The input is empty. Please give the correct input")
        return input_item_name(prompt_text)
    
def input_number(prompt_text):
    """ Prompt the user for a valid numerical input.
    Specifically, used for price and quantity.

    Parameters:
    -----------
    prompt_text : str
        Text prompt displayed to the user.

    Exceptions:
    -----------
    ValueError:
        If the value of price or quantity can not convert into float.

    Returns:
    -----------
    float: 
        Valid numerical input provided by the user, 
        if the input could converted into float.
    """
    number = input(prompt_text)

    if input_not_empty(number):
        try:
            number = float(number)
            return number
        
        except ValueError:
            print("The input is not a number. Please give the correct input.")
            return input_number(prompt_text)
    
    else:
        print("The input is empty or only contains empty space. Please give the correct input")
        return input_number(prompt_text)

def input_not_empty(value):
    """Check if the input value is not empty or only contains empty space.

    Parameters:
    -----------
    value : str
        The input value to check.

    Returns:
    -----------
    bool: 
        True if the input value is not empty or only contains empty space, False otherwise.
    """
    if value.strip():
        return True
    
    else:
        return False

def delete_confirmation(prompt_text):
    """Asks for user confirmation to delete an/all item.

    Parameters:
    -----------
    prompt_text : str
        The text to be displayed as a prompt for confirmation.

    Returns:
    -----------
    str: 
        The user's choice ('y' for yes or 'n' for no) if the choice is y or n,
    """
    choice = input(f"Are you sure to delete {prompt_text}? (y/n) ").lower()

    if choice=='y' or choice=='n':
        return choice
    
    else:
        print("Please input y or n")
        return delete_confirmation(prompt_text)

def main():
    customer = Transaction()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice in MENU:
            if choice=='1':  # If the choice is 1, add an item to the customer's cart
                print("=== Add an item to the cart ===")

                item_name = input_item_name('Item Name: ')
                quantity = input_number('Quantity: ')
                price = input_number('Price: ')

                print(customer.add_item(item_name, quantity, price))

            elif choice=='2':  # If the choice is 2, update the name of an item in the cart
                print("=== Update an item name ===")

                old_item_name = input_item_name('Item name you want to change: ')
                new_item_name = input_item_name('New Item Name: ')

                print(customer.update_item_name(old_item_name, new_item_name))
                
            elif choice=='3':  # If the choice is 3, update the price of an item in the cart
                print("=== Update an item price ===")

                item_name = input_item_name('Item Name: ')
                new_price = input_number('New Price: ')

                print(customer.update_item_price(item_name, new_price))
                
            elif choice=='4':   # If the choice is 4, update the quantity of an item in the cart
                print("=== Update an item quantity ===")

                item_name = input_item_name('Item Name: ')
                new_quantity = input_number('New Quantity: ')

                print(customer.update_item_quantity(item_name, new_quantity))
                
            elif choice=='5':  # If the choice is 5, delete an item from the cart
                print("=== Delete an item ===")
                item_name = input_item_name("Item Name: ")
                confirmation = delete_confirmation(item_name)

                if confirmation == 'y':
                    print(customer.delete_item(item_name))

                else:
                    print(f"Delete {item_name} cancelled")  # If choice is n (no), cancel the delete process
                
            elif choice=='6':   # If the choice is 6, reset the transaction (empty the cart)
                print("=== Delete all items in the cart ===")
                confirmation = delete_confirmation("all items")

                if confirmation == 'y':
                    print(customer.reset_transaction())

                else:
                    print("Delete all items cancelled") # If choice is n (no), cancel the delete process

            elif choice=='7':  # If the choice is 7, display the cart
                print("=== Display cart ===")
                cart_contain = customer.check_order() 

                if type(cart_contain) == dict:  #If the cart is not empty, print the transaction ID and the cart contents
                    print(f"Transaction ID: {cart_contain['Transaction ID']}")
                    print(f"{cart_contain['Cart']}")

                else:  #If the cart is empty, print message
                    print(cart_contain)

            elif choice=='8':  # If the choice is 8, calculate the total price of the items in the cart
                print("=== Display total ===")
                total = customer.total_price()

                if type(total) == dict:
                    for key, value in total.items():
                        print(f"{key}: {value}")

                else:
                    print(total)
                    
            elif choice=='0':  # If the choice is 0, exit the program
                sys.exit()

        else:
            print("Invalid choice. Please try again.")

        print()

if __name__ == '__main__':
    main()