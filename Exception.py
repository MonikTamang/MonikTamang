# Exception Handling
# try block is used when error will occur
'''
try:
    print(x) # x is undefined so throws exception
# except will generate a message to solve the exception 
except:
    print("x is not defined.")

# IndexError
    
try:
    even_numbers = [2, 4, 6, 8]
    print(even_numbers[5])

except IndexError:
    print('Array Index out of Bound.')

try:
    num = 10
    num = num / 0
except ZeroDivisionError:
    print('Cannot divide by 0.')
finally:
    print('This is finally block.')
'''
'''
try:
    helloworld()
except RuntimeError as error: # creating exceptino during runtime
    print(error)
'''
'''
try:
    with open("file.log") as file:
        read = file.read()

except FileNotFoundError as fnf_error:
    print(fnf_error)
'''
# specify the error type as try block will only catch error and except will show same message for any error

try:
    my_function()
    with open("File.log") as file:
        read = file.read()
except FileNotFoundError as fnf_error:
    print(fnf_error)
except RuntimeError as error:
    print(error)