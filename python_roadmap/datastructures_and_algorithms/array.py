# Different Ways to import Array:
# import array
# import array as arr       # arr acts as an alias name with the array constructor
# from array import *     # import all the functions of the array

# define a Array variable,  Example: variable = ('datatype',[values]) 
# where datatype 'i' = integer, 'd' = double and so on...

import array as arr

array_int = arr.array('i', [100, 200, 300, 400, 500]) # array integer
array_double = arr.array('d', [1.2, 2.2, 3.2]) # array double

print(array_int)
print("Length of array:", len(array_int))

print(array_double)
print(len(array_double))

# using array index to find numbers
print("Array 1st element:", array_int[0]) # first item
print("Array last element:", array_int[-1]) # last item
print("Array second last element:", array_int[-2]) # second last item


# find number index using index() function
print("Number Index number:", array_int.index(300))
# print("Number Index number:", array_int.index(600))   # if not in the array show error

# using range() in array
print("All values of array:")
for i in range(len(array_int)):
    print(array_int[i])

# slice array
print(array_int[:2]) # by default 0
print(array_int[1:3])

# change value
array_int[1] = 99 
print(array_int)

# add new value in array
# append() -> one item at a time
array_int.append(600)
print(array_int)

# extend() -> add multiple item or list of items at a time
array_int.extend([700,800,900])
print(array_int)

# insert() -> insert at specific poisition of the array
# doesnot remove the value  but shift it by one 
array_int.insert(1,200) #(position, value)
print(array_int)

# remove() -> remove the value/ doesnot give error if no value found
array_int.remove(99) 
print(array_int)

# pop() -> pop the position in the array
array_int.pop(-1)  # -1 indicates the last value in the array
print(array_int)



