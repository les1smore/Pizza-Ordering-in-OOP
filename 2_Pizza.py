#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class crust_type(Enum):
    """Assign numbers to each different pizza type"""
    thin = 0
    thick = 1

class Pizza():
    def __init__(self, toppings, cost):
        self.toppings = []
        self.cost = cost
        self.sold = False
        self.__discount = None
        self.__price = 20

    def add_toppings(toppings):
        """Add toppings"""
        self.toppings.append(toppings)
    
    def rm_toppings(toppings):
        """Remove toppings"""
        self.toppings.remove(toppings)
    
    def set_discount(self,value):
        """Set discount for pizza"""
        self.__discount = value
    
    def get_price(self):
        """Get the pizza price: specifying with/without the discount"""
        if self.__discount is None:
            return self.__price
        else:
            return self.__price * (1 - self.__discount)
    
    def update_price(self, new_price):
        """Update the pizza price only when it's not sold as a marketing campaign"""
        if self.sold:
            raise MethodFailed("We can't update the sale price of this pizza since it's been sold.")
        self.price = new_price
    
    def sale_record(self):
        """Make sure the pizza order is made and profit is returned"""
        self.sold = True
        profit = self.price - self.cost
        print('The profit of this order is:', profit)
    
    def crust_type(cru_type):
        """Specify the crust type of pizzas"""
        self.cru_type = cru_type
        
    def __repr__(self):
        return f"Toppings:{self.toppings()}, Price: {self.price()}, Profit:{self.profit()}, Crusty Type: {self.CrustyType()}"

    def __str__(self):
        pizza_str = """
            PizzaToppings:{toppings}
            Cost: {cost} 
            Customer: {customer}
            OrderDate: {order_date}""".format(toppings = self.topppings,
                                              cost = self.cost)
        return pizza_str
    
    
    

