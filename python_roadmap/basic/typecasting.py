# Implicit Type Conversion

a = 7 
print(type(a)) # type int

b = 3.0
print(type(b)) # type float

# automatically convert the type form lower data type to higher datatype
c = a + b
print(c)
print(type(c)) # type float


# Explicit Type Conversion
num_string = '12'
print(type(num_string)) # type string

num_integer = 23
print(type(num_integer)) # type int

num_string = int(num_string) # convert string to int manually
num_sum = num_integer + num_string # sum 
print(num_sum)
print(type(num_sum)) # type int
