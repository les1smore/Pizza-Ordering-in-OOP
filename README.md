# DATA 690 Final Project: Specified Classes for a Pizza Franchise

## Part 1
### Class PizzaOrder
- Ability to add/remove pizza(s)
    - An order can have more than one pizza.
- Ability to specify the store for which the order is made
- Ability to apply special promotion code
- Ability to check the order status
    - Possible statuses are ORDER_CREATED, ORDER_CANCELED, ORDER_READY, ORDER_ON_DELIVERY, ORDER_COMPLETE
- Has customer information

### Sorting and Searching
- Sort the pizza order by order date and total order amount
- Search the pizza order by customer 
- Search the pizza order by order date
- Pull a list of pizza order before a certain date in sorted order by date
- Pull a list of pizza order after a certain date in sorted order by date

## Part 2
### Class Pizza
- Ability to specify toppings
    - Ability to add/remove toppings
- Ability to specify price
- Ability to specify crust type (thin/thick)

## Part 3
### Class Store
- Ability to hold a list of employees
    - Ability to add/remove employees
- Needs to have address including zip code
- Needs to have phone number
- Needs to be able to show monthly pizza sales
- Generates a summary of the store
- Shows the number of customers that have been served 
- Increments the number of customers who've been served

## Part 4
### Class Employee
- Has a global variable minimal wage and to make sure the salary level is legitimately acceptable
- Has first name, last name
- Has employee id, email, location, and the login attempt times
- Has a profile summary for each employee
- Has a greeting at the start of every log-in
- Increments the value of login attempts
- Resets the login attempts
- Has a method to read the data from a file

### Class Manager
- has basic information recorded like other employees
- has access privileges displayed

## Part 5
### Class Customer
- Has first name, last name, phone number, zip code, frequent mileage number
- A customer must be able to find one of your stores in the same zip code

## Part 6 Testing
- Prepare the testing data
- Test the pizza orders of all customers
