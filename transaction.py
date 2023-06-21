import datetime
import pandas

class Transaction:
    """Represents a transaction for a cashier program.

    Attributes:
    -----------
    DISCOUNTS : dict
        A dictionary that defines discount thresholds and corresponding discount percentages.
        The keys represent the total cart value threshold, and the values represent the discount percentage.
        The discounts are applied based on the total price of the items in the cart.
        For example, if the total price exceeds 500000, a 10% discount will be applied.
    id_transaction : str 
        The ID of the transaction, generated based on the current date and time.
    cart : pandas.DataFrame
        The shopping cart containing the items in the transaction.

    Methods
    -----------
    add_item(item_name, quantity, price)
        Adds an item to the shopping cart.
    update_item_name(old_item_name, new_item_name)
        Updates the name of an item in the shopping cart.
    update_item_quantity(item_name, new_quantity)
        Updates the quantity of an item in the shopping cart.
    update_item_price(item_name, new_price)
        Updates the price of an item in the shopping cart.
    delete_item(item_name)
        Deletes an item from the shopping cart.
    reset_transaction()
        Resets the transaction by emptying the shopping cart.
    is_in_cart(item_name)
        Check if the item is exist in the cart.
    check_order()
        Displaying the transaction ID and the contents of the shopping cart.
    total_price()
        Calculates the total price of the items in the shopping cart, including any applicable discounts.
    """

    DISCOUNTS = {
                500_000:10/100,
                300_000:8/100,
                200_000:5/100
                } 

    def __init__(self):
        """  Initializes a new instance of the Transaction class.
        Parameters:
        -----------
        id_transaction : str
            The ID of the transaction, generated based on the current date and time.
        cart : pandas.DataFrame
            The shopping cart containing the items in the transaction.
        """
        self.id_transaction = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
        self.cart = pandas.DataFrame(columns=[
                                              "Item Name",
                                              "Quantity",
                                              "Price/Item",
                                              "Total Price/Item"
                                             ])

    def add_item(self, item_name, quantity, price):
        """ Adds a new item to the cart with the provided name, quantity, and price.
        It calculates the total price for the item and appends it to the cart DataFrame.
        If the item is already in the cart, it returns an appropriate message.

        Parameters:
        -----------
        item_name : str
            The name of the item.
        quantity : float
            The quantity of the item.
        price : float
            The price of the item.

        Exceptions:
        -----------
        ValueError:
            If the value of price or quantity can not convert into float.

        Returns:
        -----------
        message : str
            A message indicating the success or failure of adding the item to the cart.
        """
        status = self.is_in_cart(item_name)
        
        if status:
            message = f"{item_name} already in the cart. Choose display to show your cart"
            return message
                        
        else:
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
            

    def update_item_name(self, old_item_name, new_item_name):
        """ Updates the name of an item in the cart from the old name 
        to the new name if it is exist in the cart.
        If the item does not exist in the cart, it returns an appropriate message.

        Parameters:
        -----------
        old_item_name : str
            The current name of the item.
        new_item_name : str
            The new name for the item.

        Returns:
        -----------
        str: 
            A message indicating whether the update was successful or an error message.
        """
        status = self.is_in_cart(old_item_name)

        if status:
            self.cart.loc[self.cart['Item Name']==old_item_name, 'Item Name'] = new_item_name

            message = f"Update {old_item_name} to {new_item_name} success"
            return message
        
        else:
            message = f"Product {old_item_name} does not exist"
            return message

    def update_item_quantity(self, item_name, new_quantity):
        """ Updates the quantity of an item in the cart to the new quantity if it is exist in the cart.
        If the item does not exist in the cart, it returns an appropriate message.
        If the new quantity is not a valid number, it returns an error message.

        Parameters:
        -----------
        item_name : str
            The name of the item.
        new_quantity :float
            The new quantity for the item.

        Exceptions:
        -----------
        ValueError:
            If the value of quantity can not convert into float.

        Returns:
        str: 
            A message indicating whether the update was successful or an error message.
        """
        status = self.is_in_cart(item_name)

        if status:
            try:
                new_quantity = float(new_quantity)

                self.cart.loc[self.cart['Item Name']==item_name, 'Quantity'] = new_quantity
                price = self.cart.loc[self.cart['Item Name']==item_name, 'Price/Item'].values[0]
                self.cart.loc[self.cart['Item Name']==item_name, 'Total Price/Item'] = new_quantity * price

                message = f"Update quantity of {item_name} success"
                return message

            except ValueError:
                message = "Quantity is not a number"
                return message
            
        else:
            message = f"Product {item_name} does not exist"
            return message

    def update_item_price(self, item_name, new_price):
        """ Updates the price of an item in the cart to the new price if it is exist in the cart.
        If the item does not exist in the cart, it returns an appropriate message.
        If the new price is not a valid number, it returns an error message.

        Parameters:
        -----------
        item_name : str
            The name of the item.
        new_price : float
            The new price for the item.

        Exceptions:
        -----------
        ValueError:
            If the value of quantity can not convert into float.

        Returns:
        -----------
        str: 
            A message indicating whether the update was successful or an error message.
        """
        status = self.is_in_cart(item_name)
        if status:
            try:
                new_price = float(new_price)

                self.cart.loc[self.cart['Item Name']==item_name, 'Price/Item'] = new_price
                quantity = self.cart.loc[self.cart['Item Name']==item_name, 'Quantity'].values[0]
                self.cart.loc[self.cart['Item Name']==item_name, 'Total Price/Item'] = quantity * new_price

                message = f"Update price of {item_name} success"
                return message

            except ValueError:
                message = "Price is not a number"
                return message
            
        else:
            message = f"Product {item_name} does not exist"
            return message            

    def delete_item(self, item_name):
        """ Removes an item from the cart based on the provided item name.
        If the cart is empty or the item is not exist, it returns an appropriate message.
        If the item is exist in the cart, it returns the item was successfully deleted

        Parameters:
        -----------
        item_name : str
            The name of the item.

        Returns:
        -----------
        str: 
            A message indicating whether the item was successfully deleted or an error message.
        """

        if self.cart.empty:
            message = "Cart is empty"
            return message
        
        else:
            status = self.is_in_cart(item_name)

            if status:
                item_index = self.cart[self.cart["Item Name"] == item_name].index
                self.cart = self.cart.drop(item_index)
                self.cart = self.cart.reset_index(drop=True)

                message = f"Product {item_name} is deleted"
                return message
            
            else:
                message = f"Product {item_name} does not exist"
                return message
          
    def reset_transaction(self):
        """ Resets the transaction by clearing the cart.
        If the cart is empty, it returns an appropriate message.

        Returns:
        -----------
        str: 
            A message indicating whether the cart was successfully reset or an error message.
        """
        if self.cart.empty:
            message = "Cart is empty"
            return message
        
        else:
            self.cart = self.cart.drop(self.cart.index)
            message = "All items in Cart deleted"
            return message

    def is_in_cart(self, item_name):
        """ Check if the item is in the cart.

        Parameters:
        -----------
        item_name : str
            The name of the item.

        Returns:
        -----------
        status: bool
            If the item is in the cart, return False,
            otherwise return True.
        """
        status = self.cart['Item Name'].isin([item_name]).any()
        return status 
   
    def check_order(self):
        """ This method checks the current order in the cart.
        If the cart is empty, it returns an appropriate message.
        If the cart is not empty, it returns the transaction ID and the cart contents.

        Returns:
        -----------
        dict: 
            A dictionary containing the transaction ID and the cart DataFrame if the cart is not empty.
        str:
            A message indicating whether the cart is empty.
        """
        if self.cart.empty:
            message = "Cart is empty"
            return message
        
        else:
            self.cart = self.cart.reset_index(drop=True)
            self.cart = self.cart.rename_axis('No')
            self.cart.set_index(self.cart.index+1, inplace=True)
            return {"Transaction ID" : self.id_transaction, 
                    "Cart": self.cart}
        

    def total_price(self):
        """ Calculates the total price of the cart by summing the total price of each item.
        It applies any applicable discounts based on the predefined DISCOUNTS dictionary.
        It returns the total price, discount percentage, and total price after discount.
        If the cart is empty, it returns an appropriate message.

        Returns:
        dict: 
            A dictionary containing the total price, discount, and total price after discount.
        str:
            A message indicating whether the cart is empty.
        """
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