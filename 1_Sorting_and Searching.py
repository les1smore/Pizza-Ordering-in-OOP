#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import datetime
# Sort the pizza order by order date
def sort_by_order_date(pizza_order):
    """Timsort: a hybrid sorting algorithm that derived from merge sort and insertion sort.
       Computing Complexity: O(n.logn)"""
    pizza_order.sort(key=lambda order_date: datetime.datetime.strptime(order_date, '%Y-%m-%d'))
    
# Sort the pizza order by total order amount
def sort_by_amount(pizza_order):
    """Selection Sort: iterates all the amount of pizza order list. If the smallest element shows up then it will swap with the first one.
       Computing Complexity: O(n^2)"""
    for i in range(len(pizza_order) - 1): #iterating n-1 times
        minimum = i 
        for j in range(i + 1, len(pizza_order)): # Compare i+1 and i
            if(pizza_order[j] < pizza_order[minimum]):
                minimum = j
        if (minimum != i):
            pizza_order[i], pizza_order[minimum] = pizza_order[minimum], pizza_order[i]
    return pizza_order

# Search the pizza order by customer
def search_by_customer(customer,pizza_order):
    """Linear Search: A searching algorithm that sequentially checks each element of a list until finding the matched result.
       Computing Complexity: O(n)"""
    p = 0 # initialize the position
    global iterations
    i = 0 # initialize the iteration
    while p < len(pizza_order):
        i += 1
        if cusotmer == pizza_order[p]:
            return "Customer is found."
        p += 1 
    return "Customer is not found."

# Search the pizza order by the order date
def search_by_order_date(date, pizza_order):
    """Linear Search: A searching algorithm that sequentially checks each element of a list until finding the matched result.
       Computing Complexity: O(1)"""
    for order in pizza_order:
        if order.order_date == date:
            return order
    return "Order date is not found."
        
# Pull a list of pizza order before a certain date in sorted order by date
def order_before_date(date, pizza_order):
    """Linear Search: A searching algorithm that sequentially checks each element of a list until finding the matched result.
       Computing Complexity: O(1)"""
    pizza_order = pizza_order.sort(key=lambda order_date: datetime.strptime(order_date, '%d-%b-%y'))
    for i in range(len(pizza_order)):
        if pizza_order[i].order_date < date:
            return pizza_order[:i]
    return "The input order date is the earliest one on the record."

# Pull a list of pizza order after a certain date in sorted order by date
def order_after_date(date, pizza_order):
    """Linear Search: A searching algorithm that sequentially checks each element of a list until finding the matched result.
       Computing Complexity: O(1)"""
    pizza_order = pizza_order.sort(key=lambda order_date: datetime.strptime(order_date, '%d-%b-%y'))
    for i in range(len(pizza_order)):
        if pizza_order[i].order_date > date:
            return pizza_order[i:]
    return "The input order date is the lastest one on the record."

