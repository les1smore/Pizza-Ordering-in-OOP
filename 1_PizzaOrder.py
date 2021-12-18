#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from enum import Enum
class OrdStatus(Enum):
    """Assign numbers to each different pizza order status"""
    ORDER_CANCELED = 0
    ORDER_CREATED = 1
    ORDER_READY = 2
    ORDER_ON_DELIVERY = 3
    ORDER_COMPLETE = 4
    
class AmountError(Exception):
    pass


class PizzaOrder():
    def __init__(self, pizza, store, pro_code, customer, order_date, amount):
        self.pizza = []
        self.store = store
        self.pro_code = pro_code
        self.customer = customer
        self.order_date = order_date
        self.amount = int(amount)
        
        if amount < 0: # To make sure the amount is positive
            raise AmountError("The amount of order has to be positive.")
        else:
            self.amount = amount
        
    def add_pizza(pizza):
        """Add pizzas"""
        self.pizza.append(pizza)
    
    def rm_pizza(pizza):
        """Remove pizzas"""
        self.pizza.remove(pizza)
    
    def get_amount(amount):
        """Get the amount of the pizza order"""
        return float(self.amount)
    
    def set_store(store):
        """Specify the store for which the order is made"""
        self.store = store
    
    def set_pro_code(pro_code):
        """Apply special promotion code"""
        self.pro_code = pro_code
    
    def order_status(ord_status):
        """Specify and check the order status of each pizza"""
        self.ord_status = ord_status   
    
    def customer(customer):
        """Load in customer information"""
        self.customer = customer
    
    def set_order_date(self, order_date):
        """Set the order date as a string representative of a date"""
        self.order_date = order_date
    
    def get_order_date(self, order_date):
        return self.order_date
    
    def __str__(self):
        order_str = """
            Amount:{amount}
            Store: {store} 
            Customer: {customer}
            OrderDate: {order_date}
            ProCode: {pro_code}""".format(amount = self.amount, store = self.store, customer = self.customer,
                                          order_date = self.order_date, pro_code = self.pro_code
                                         )
        return order_str
    
    

