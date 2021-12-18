#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Customer(object):
    def __init__(self, first_name = '', last_name = '', phone_num = None, 
               zip_code = None, freq_mil_num = None):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_num = phone_num
        self.zip_code = int(zip_code)
        self.freq_mil_num = int(freq_mil_num)
    
    def find_store(store):
        target = []
        while self.zip_code != None:
            for i in store:
                if store.address.zip_code == self.zip_code:
                    target.append(target)
                return target
    def __str__(self):
        cust_str = """
        Name: {name} 
        Contact: {phone_num}
        Address: {zip_code}
        Frequent Milleage Number: {freq_mil_num}""".format(name = self.first_name + self.last_name,
                                                           phone_num = self.phone_num, zip_code = self.zip_code,
                                                          freq_mil_num = self.freq_mil_num)
        return cust_str
              

