class Employee: # class
    pass    # no attribues and methods

# creating objects
emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)

emp_1.first = 'Hello'
emp_1.last = 'World'
emp_1.email = 'helloworld@gmail.com'

emp_2.first = 'John'
emp_2.last = 'Cena'
emp_2.email = 'johncena@gmail.com'

print(emp_1.email)
print(emp_2.email)


# constructor or initilizer
class employee: # class
    # constructor
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@gmail.com'

    # using self in class methods
    def emp_details(self):
        print("First Name: ", self.first)
        print("Last Name: ", self.last)
        print("Email: ", self.email)

# creating objects
emp_1 = employee('John', 'Cena')
emp_1.emp_details

emp_2 = employee('John', 'Wick')
emp_2.emp_details
