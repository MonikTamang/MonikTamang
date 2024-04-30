# define a function
def my_function():
    print("hello_World")

my_function() # call the function

# pass variable
def print_Name(name):
    print("Your name: ", name)

name = input("Enter your name: ")
print_Name(name)

# pass multiple  variable
def two_variable(a, b):
    print('Sum:', a + b)

two_variable(a = 20, b = 40) # must use same variable name as function


# arbitary arguments
# if you donot know how many arguments you want to pass
def multiple_values(*values):
    print(values[2])

multiple_values('apple', 'ball', 'cat')

# key word aruguments
def key_function(child1, child2, child3):
    print('The eldest', child1)

key_function(child1 = 'Thulo', child2 = 'bichko', child3 = 'Kancho')


# if donot know how many variable in key arguments
def key_mulitple_values_function(**name):
    print(name['lastname'])
key_mulitple_values_function(firstname = "Monik", lastname = "Tamang")

# incase of dufault function it provides the value in the parameter
def country_function(country = 'Nepal'):
    print("Country: " + country)

country_function("India")
country_function()
country_function("Brazil")
country_function()

# passing list
def list_function(food):
    for x in food:
        print(x)

fruits = ['apple', 'banana', 'mango']
list_function(fruits)

# return values
def return_function(x):
    return x * 5
print(return_function(3))
print(return_function(5))

# pass statement
def pass_function():
    pass # use when you need empty function as function cannot be empty you need to use pass

# only positional function not key value funciton
# postitional function(3, 4), keyvalue function(a = 3, b = 4)

def position_only_funciton(a, b, /):
    return a * b

print(position_only_funciton(3, 4))
# print(position_only_funciton(a = 3, b = 4)) --> generates TypeError due to keyvalue

# keyword only function:
def keyword_only_function(*, a, b):
    return a * b

print(keyword_only_function(a = 3, b = 5))
# print(keyword_only_function(3, 4)) --> generates TypeError due to position

# using both keyvalue and position
def both_function(a , b, /, *, c, d):
    print('Total: ' , a + b+ c + d)

both_function(1, 2, c = 3, d = 4)
        