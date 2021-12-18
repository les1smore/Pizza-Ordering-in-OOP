#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Store():
    def __init__(self, employees, address, tel_num, sale, name):
        self.employees = []
        self.address = address
        self.tel_num = str(tel_num)
        self.sale = []
        self.num_served = 0
        self.name = name

    
    def add_emp(employees):
        """Add employees"""
        self.employees.append(employees)
    
    def rm_emp(employees):
        """Remove employees"""
        self.employees.remove(employees)
    
    def set_address(address, zip_code):
        """Have address including zip code"""
        self.address = str(address)
        self.zip_code = int(zip_code)
    
    def get_monthly_sale():
        """Show monthly pizza sales"""
        sort_by_order_date(self.sale)
        month = self.sale[0].order_date.month # Determine the specific month
        while len(self.sale) > 0:
            amount = 0 # initialize the amount 
            i = 0 # initialize the iteration time
            while self.sale[i].order_date.month == month:
                if i < len(self.sale):
                    amount += self.sale[i].amount
                    i += 1
            print('The monthly sale for',month, 'is',amount,'.')
    
    def describe_store(self):
        intro = self.name + " serves delicious " + self.cru_type + " pizza. "
        print("\n" + intro)
    
    def set_num_served(self, num_served):
        """Show the number of customers that have been served"""
        self.num_served = num_served
    
    def increment_num_served(self, add_served):
        """Increment the number of customers who've been served"""
        self.num_served += add_served

