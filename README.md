# Super-Cashier
Super Cashier is a program created to fulfill the completion of my course on Analytics and Data Science course at Pacmann.


## Problems Background
Andi, the owner of a supermarket, wants to implement a self-service cashier system for his store. With this self-service system, customers will be able to calculate their total purchases independently. Andi needs help from a programmer to make this self-service cashier.


## Requirements
The self-service cashier requires the following features:
- Generate a transaction ID when a customer initiates a transaction.
- Allow customers to add items to the shopping cart.
- Allow customers to update the name, price, and quantity of items in the shopping cart.
- Allow customers to remove items from the shopping cart.
- Allow customers to clear the entire shopping cart.
- Display the contents of the shopping cart.
- Calculate the total purchase price, including applicable discounts. The discount rules are as follows:
  + If the total purchase amount exceeds Rp. 200,000, apply 5% discount.
  + If the total purchase amount exceeds Rp. 300,000, apply 8% discount.
  + If the total purchase amount exceeds Rp. 500,000, apply 10% discount.
- Provide error messages for user input errors.


## Flowchart
This section explains the flowchart for creating the self-service cashier, which will be referred to as the **Super Cashier**.
The flowchart consists of several sub-flowcharts, namely the main menu, add item, update item name, update item price, update item quantity, delete an item, delete all items in the cart, show cart, and calculate total.

### Main Menu Flowchart
![Main Menu Flowchart](https://github.com/aquemos/Super-Cashier/blob/main/image/main%20menu.png)

### Add Item Flowchart
![Add Item Flowchart](https://github.com/aquemos/Super-Cashier/blob/main/image/add%20item.png)

### Update Item Name Flowchart
![Update Item Name Flowchart](https://github.com/aquemos/Super-Cashier/blob/main/image/update%20item%20name.png)

### Update Item Price Flowchart
![Update Item Price Flowchart](https://github.com/aquemos/Super-Cashier/blob/main/image/update%20item%20price.png)

### Update Item Quantity Flowchart
![Update Item Quantity Flowchart](https://github.com/aquemos/Super-Cashier/blob/main/image/update%20item%20quantity.png)

### Delete an Item Flowchart
![Delete an Item Flowchart](https://github.com/aquemos/Super-Cashier/blob/main/image/delete%20an%20item.png)

### Delete All Items Flowchart
![Delete All Items Flowchart](https://github.com/aquemos/Super-Cashier/blob/main/image/delete%20all%20items.png)

### Show Cart Flowchart
![Show Cart Flowchart](https://github.com/aquemos/Super-Cashier/blob/main/image/show%20cart.png)

### Calculate Total Flowchart
![Calculate Total Flowchart](https://github.com/aquemos/Super-Cashier/blob/main/image/calculate%20total.png)


## Code Explanation
The program code is divided into two files, i.e., **script.py** and **transaction.py**.

### script.py
There are several functions in this file, such as display_menu, input_item_name, input_number, input_not_empt, delete_confirmation, and main. Here the explanation of each function code.

#### display_menu
```python
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
```
The code snippet above defines a dictionary called *MENU* that stores options for a cashier program. Each option is represented by a key-value pair, where the key is a string representing the option number and the value is a string representing the description of the option.

The *display_menu()* function is defined to display the menu to the user. It does not take any arguments and has no return value. The function prints a heading indicating the program menu ("===== Cashier Program Menu ====="), and then iterates over the items in the *MENU* dictionary using a for loop.

#### input_item_name
```python
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
```


## Test Case


## Conclusion
