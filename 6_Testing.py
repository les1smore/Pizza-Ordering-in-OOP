#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Prepare the testing data
Stores = [Store(employees = [Employee('Chloe','Benben','1', '123@umbc.com','Rockville',100), 
                             Employee('Gagin', 'Boboly','2', '456@umd.come','Baltimore',55), 
                             Employee('Cecilia', 'Sarah','3', '887@qq.com','Bethesda', 34)],
                address = ('Rockville', 20850), tel_num = '556-345-890', sale = 500, name = 'Store1'),
          
          Store(employees = [Employee('Princey', 'BooPoo', '4', '879@umbc.com', 'Baltimore', 78),
                             Employee('Rose','Rosslyn','5', '224@umbc.com', 'Baltimore City', 9),
                             Employee('Alice', 'Wonder', '6', '897@umbc.com', 'Silver Spring', 80)],
               address = ('Baltimore', 21201), tel_num = '001-987-675', sale = 450, name = 'Store2'),
          Store(employees = [Employee('Evelyn','Adams', '7', 'eam@umbc.com', 'Bethesda', 99),
                             Employee('Doris','Obron','8','ioi@umbc.com', 'Bethesda', 109),
                             Employee('Wendy', 'Tutle','9', 'wti@umbc.com', 'Bethesda', 203)],
               address = ('Bethesda', 20810), tel_num = '789-098-342', sale = 331, name = 'Store3')
         ]

Customers = [Customer('Zandaya', 'Peter', '887-435-332', 56709, 500),
             Customer('Bog', 'Greg', '990-890-654', 89702, 654),
             Customer('Posa', 'Parker', '456-333-122', 19786, 202)
            ]

Orders = [PizzaOrder(pizza=[Pizza(toppings = ['Pepperoni'], cost = 10),
                            Pizza(toppings = ['Margherita'], cost = 12),
                            Pizza(toppings = ['Capricciosa'], cost = 11)],
                     store = Stores[0], pro_code = 'ILovePizza', customer = Customers[0],
                     order_date = datetime.date(2021,7,8).strftime('%Y-%m-%d'), amount = 2),
          PizzaOrder(pizza = [Pizza(toppings = ['Margherita'], cost = 12)],
                    store = Stores[1], pro_code ='GOGO2021', customer = Customers[1],
                    order_date = datetime.date(2021,9,10).strftime('%Y-%m-%d'), amount = 5),
          PizzaOrder(pizza = Pizza(toppings = ['Capricciosa'], cost = 11),
                     store = Stores[2], pro_code = 'HPNEWYEAR', customer = Customers[2],
                    order_date = datetime.date(2021,10,12).strftime('%Y-%m-%d'), amount = 1)
         ]        

