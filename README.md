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

#### display_menu function
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
    print("===== Cashier Program Menu =====")
    
    for key, value in MENU.items():
        print(f"{key}. {value}")
```
The code snippet above defines a dictionary called *MENU* that stores options for a cashier program. Each option is represented by a key-value pair, where the key is a string representing the option number and the value is a string representing the description of the option.

The *display_menu()* function is defined to display the menu to the user. It does not take any arguments and has no return value. The function prints a heading indicating the program menu ("===== Cashier Program Menu ====="), and then iterates over the items in the *MENU* dictionary using a for loop.

#### input_item_name function
```python
def input_item_name(prompt_text):
    item_name = input(prompt_text)

    if input_not_empty(item_name):
        return item_name.capitalize()
    
    else:
        print("The input is empty. Please give the correct input")
        return input_item_name(prompt_text)
```
This function is used to prompt the user to input an item name. It takes one parameter, namely the prompt text to be displayed to the user.

The function follows a recursive approach to handle input validation. It first prompts the user to enter an item name using the *input()* function and storing the result in the *item_name* variable.

Next, it calls a function named *input_not_empty(item_name)* to check if the input is not empty. If the input is not empty, the function capitalizes the item name using the *capitalize()* method and returns it. Otherwise, the function displays a message indicating that the input is empty and prompts the user again by calling the *input_item_name(prompt_text)* function recursively. This means the function will continue asking for input until a non-empty value is provided.

#### input_number function
```python
def input_number(prompt_text):
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
```
This function prompts the user for a valid numerical input. The function takes one parameter, i.e., the text prompt displayed to the user. This function is used to get the input for price and quantity.

The function follows a recursive approach to handle input validation. It first prompts the user to enter a number using the *input()* function and storing the result in the *number* variable.

Next, it calls a function named *input_not_empty(item_name)* to check if the input is not empty. If the input is not empty, the function attempts to convert the number variable to a float using the *float()* function. While, if the input is empty, the function displays a message indicating that the input is empty and prompts the user again by calling *input_number(prompt_text)* function again.

If the conversion of input to float is success, the function returns the converted number. If ValueError raised during the conversion, the function displays a message indicating that the input is not a number, and it calls *input_number(prompt_text)* recursively.

#### input_not_empty function
```python
def input_not_empty(value):
    if value.strip():
        return True
    
    else:
        return False
```
This function checks if an input value is not empty or only contains empty spaces. The function takes one input argument to be checked. To check if the input is not empty, the *strip()* method is used. If the input is not empty, it will return True. Otherwise, return False.

#### delete_confirmation function
```python
def delete_confirmation(prompt_text):
    choice = input(f"Are you sure to delete {prompt_text}? (y/n) ").lower()

    if choice=='y' or choice=='n':
        return choice
    
    else:
        print("Please input y or n")
        return delete_confirmation(prompt_text)
```
This function prompts the user for confirmation before deleting an item or all items. It takes one parameter, i.e., text to be displayed as a prompt for confirmation. 

It first prompts the user to enter a 'y' (yes) or 'n' (no) using the *input()* function and storing the result in the *choice* variable. If the input value is 'y' or 'n', it will return the choice. If the user's choice is not 'y' or 'n', the function prints an error message instructing the user to input either 'y' or 'n'. It then recursively calls delete_confirmation(prompt_text).

#### main function
```python
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
```

The main function serves as the central control flow of the program, interacting with the user and executing different functionalities based on their choices. It utilizes an instance of the Transaction class named customer to manage the transaction and cart operations.

The function follows a loop structure, repeatedly displaying the menu options, accepting user input, and executing the corresponding function based on the user's choice.

### transaction.py
This file contains a Transaction class that is designed to handle transactions for a cashier program. It provides methods for managing a shopping cart, including adding, updating, and deleting items, as well as calculating the total price and applying discounts.

#### Class attribute
```python
DISCOUNTS = {
                500_000:10/100,
                300_000:8/100,
                200_000:5/100
                } 
```
DISCOUNTS is a dictionary that defines discount thresholds and corresponding discount percentages. The keys represent the total cart value threshold, and the values represent the discount percentage. The discounts are applied based on the total price of the items in the cart.

#### Instance attribute
```python
def __init__(self):
        self.id_transaction = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
        self.cart = pandas.DataFrame(columns=[
                                              "Item Name",
                                              "Quantity",
                                              "Price/Item",
                                              "Total Price/Item"
                                             ])
```
When a new instance of the Transaction class initializes, the transaction ID and empty data frame of the cart are generated. The transaction ID is generated based on the current date. The shopping cart contains the following columns:

- "Item Name": The name of the item.
- "Quantity": The quantity of the item.
- "Price/Item": The price of each item.
- "Total Price/Item": The total price of the item (quantity multiplied by price).

#### add_item method
```python
    def add_item(self, item_name, quantity, price):
        index_item = self.get_item_index(item_name)
        
        if index_item.empty:
            try:
                quantity = float(quantity)

                try:
                    price = float(price)
                    total_price_item = quantity * price

                    item_data = [item_name, quantity, price, total_price_item]
                    new_product = pandas.DataFrame([item_data], columns=self.cart.columns)
                    self.cart = pandas.concat([self.cart, new_product])

                    message = f"Item name: {item_name}, Quantity: {quantity}, Price: {price} is added to cart"
                    return message
                
                except ValueError:
                    message = "Price is not a number"
                    return message
                
            except ValueError:
                message ="Quantity of item is not a number"
                return message
            
        else:
            message = f"{item_name} already in the cart. Choose display to show your cart"
            return message
```
The add_item method is used to add a new item to the shopping cart with the provided name, quantity, and price. If the item is already in the cart, a notification message that the item is already in the cart is given. If the item does not exist in the cart, the typecasting of quantity and price into float is carried out. It will return an error message if the typecasting of quantity and price is not successful. While the typecasting process is successful, the total price is calculated. The item name, price, quantity, and total price are attached to the DataFrame cart.

#### update_item_name method
```python
    def update_item_name(self, old_item_name, new_item_name):
        index_item = self.get_item_index(old_item_name)

        if index_item.empty:
            message = f"Product {old_item_name} does not exist"
            return message
        
        else:
            index_item = self.get_item_index(old_item_name)
            self.cart.loc[index_item, 'Item Name'] = new_item_name

            message = f"Update {old_item_name} to {new_item_name} success"
            return message
```
This method is used to update the name of an item in the cart from the old name to the new name if the item exists in the cart. If the item does not exist in the cart, the error message that the item does not exist is returned.

#### update_item_quantity method
```python
def update_item_quantity(self, item_name, new_quantity):
        index_item = self.get_item_index(item_name)
        if index_item.empty:
            message = f"Product {item_name} does not exist"
            return message
            
        else:
            try:
                new_quantity = float(new_quantity)

                self.cart.loc[index_item, 'Quantity'] = new_quantity
                price = self.cart.loc[index_item, 'Price/Item']
                self.cart.loc[index_item, 'Total Price/Item'] = new_quantity * price

                message = f"Update quantity of {item_name} success"
                return message

            except ValueError:
                message = "Quantity is not a number"
                return message
```
This method is used to update the quantity of an item in the cart to the new quantity if the item exists in the cart. If the item does not exist in the cart, an error message to inform that the item does not exist is returned. Additionally, if the new quantity is not a valid number, an error message to inform the new quantity is not a number is returned.

#### update_item_price quantity
```python
    def update_item_price(self, item_name, new_price):
        index_item = self.get_item_index(item_name)
        if index_item.empty:
            message = f"Product {item_name} does not exist"
            return message
            
        else:
            try:
                new_price = float(new_price)

                self.cart.loc[index_item, 'Price/Item'] = new_price
                quantity = self.cart.loc[index_item, 'Quantity']
                self.cart.loc[index_item, 'Total Price/Item'] = quantity * new_price

                message = f"Update price of {item_name} success"
                return message

            except ValueError:
                message = "Price is not a number"
                return message
```
This method is used to update the price of an item in the cart to the new price if the item exists in the cart. If the item does not exist in the cart, an error message to inform that the item does not exist in the cart is returned. Additionally, if the new price is not a valid number, an error message that informs the price is not a number is returned.

#### delete_item method
```python
def delete_item(self, item_name):
        if self.cart.empty:
            message = "Cart is empty"
            return message
        
        else:
            index_item = self.get_item_index(item_name)

            if index_item.empty:
                message = f"Product {item_name} does not exist"
                return message
            
            else:
                item_index = self.cart[self.cart["Item Name"] == item_name].index
                self.cart = self.cart.drop(item_index)
                self.cart = self.cart.reset_index(drop=True)

                message = f"Product {item_name} is deleted"
                return message
```
This method is used to remove an item from the cart based on the provided item name. If the cart is empty, it will return a message that the cart is empty. If the item does not exist in the cart, a message that informs the item does not exist is returned. If the item exists in the cart, the method deletes the item.

#### reset_transaction method
```python
def reset_transaction(self):
        if self.cart.empty:
            message = "Cart is empty"
            return message
        
        else:
            self.cart = self.cart.drop(self.cart.index)
            message = "All items in Cart deleted"
            return message
```
This method is used to reset the transaction by clearing the cart. If the cart is empty, it returns a message indicating that the cart is empty. Otherwise, it removes all items from the cart by dropping all rows from the cart DataFrame. After clearing the cart, it returns a message indicating that all items in the cart have been deleted.

#### get_item_index method
```python
    def get_item_index(self, item_name):
        index_item = self.cart.loc[self.cart['Item Name'] == item_name].index
        return index_item 
```
This method is used to retrieve the index of an item in the cart based on its name. It takes an item_name parameter and returns a pandas Index object representing the index of the item in the cart DataFrame. 

#### check_order method
```python
def check_order(self):
        if self.cart.empty:
            message = "Cart is empty"
            return message
        
        else:
            self.cart = self.cart.reset_index(drop=True)
            self.cart = self.cart.rename_axis('No')
            self.cart.set_index(self.cart.index+1, inplace=True)
            return {"Transaction ID" : self.id_transaction, 
                    "Cart": self.cart}
```
This method is used to check the current order in the cart. If the cart is empty, it returns a message indicating that the cart is empty. If the cart is not empty, it returns a dictionary containing the transaction ID and the cart DataFrame.

#### total_price method
```python
    def total_price(self):
        if self.cart.empty:
            message = "Cart is empty"
            return message
        
        else:
            total_shopping_cart = self.cart["Total Price/Item"].sum()

            discount_percentage = 0
            total_after_discount = total_shopping_cart

            for threshold, discount in self.DISCOUNTS.items():
                if total_shopping_cart > threshold:
                    discount_percentage = discount
                    total_after_discount = (total_shopping_cart
                                            -(total_shopping_cart*discount_percentage))
                    break
            
            return {'Total': f"Rp. {total_shopping_cart:,}", 
                    'Discount': f"{int(discount_percentage*100)}%", 
                    'Total after Discount': f"Rp. {total_after_discount:,}"}
```
This method calculates the total price of the cart by summing the total price of each item. It applies any applicable discounts based on the predefined DISCOUNTS dictionary. The method returns a dictionary containing the total price, discount percentage, and total price after discount if the cart is not empty. If the cart is empty, a message to inform that the cart is empty is returned.

## How to Use

## Test Case


## Conclusion
