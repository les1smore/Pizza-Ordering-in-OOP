#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Employee(object):
    min_wage = 30000
    def __init__(self, first_name, last_name, emp_id, email, location, log_attps):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.emp_id = int(emp_id)
        self.email = email
        self.location = location.title
        self.log_attps = 0 # Initialize the login attempts for every employee
    
    def salary_check(self,salary):
        """Check the salary level to make sure it's at least above the legitimate salary level"""
        if salary >= Employee.min_wage:
            self.salary = salary
        else:
            self.salary = Employee.min_wage
    
    def get_profile(self):
        """Set up a profile summary for each employee"""
        print("\n" + self.first_name + " " + self.last_name)
        print(" Employee ID: " + self.emp_id)
        print(" Email: " + self.email)
        print(" Location: " + self.location)
    
    def welcome_emp(self):
        """Has a greeting at the start of every log in""" 
        print("\n Welcome " + self.first_name + "!")
    
    def increment_log_attps(self):
        """Increments the value of login attempts"""
        self.log_attps += 1
    
    def reset_log_attps(self):
        """Resets the login attempts"""
        self.log_attps = 0
    
    @classmethod
    def from_file(cls, file_name):
        with open(file_name, 'r') as f:
            name = f.readline()
        return cls(name)
    
class Manager(Employee):
    """A managerial role in the store"""
    def __init__(self, first_name, last_name, emp_id, email, location):
        super().__init__(first_name, last_name, emp_id, email, location)
        self.access = []
    
    def access_privileges(self):
        """Has access privileges displayed"""
        print("\n Access Privileges:")
        for p in self.access:
            print("- " + p)
            

