# --------------------------------------- creating list
list1 = ["apple", "banana"]
print(list1)
# changing value and duplication
list1[0] = "banana"
print(list1)
# use of index and ordered
print(list1[0])
# using list() constructor
listConstructor = list(("hello", "world"))
print(listConstructor)

# --------------------------------------- creating tuple
tuple1 = ("apple", "banana")
print(tuple1)

# changing value in tuple create error
# tuple1[0] = "banana" 

# accepts duplicate data
tuple1 = ("apple", "apple")
print(tuple1)
# use of index and ordered
print(tuple1[0])
# using tuple constructor
tupleConstructor = tuple(("hello", "world"))
print(tupleConstructor)

# --------------------------------------- creating set
set1 = {"apple", "banana"}
print(set1)

# sets are unindexed and unordered
# print(set1[0])

# cannot change value (doesnot support index)
# set1[0] = "banana"
# duplicate values
set1 = {"apple", "apple", False, 0, "banana"}
print(set1)
# set constructor
setConstructor = set(("hello", "world"))
print(setConstructor)

# --------------------------------------- creating dictionary
dict1 = {
    "name": "Monik", 
    "age": 23
    }
print(dict1)
# using ordered 
print(dict1["name"])
print(dict1["age"])
print(len(dict1)) # no of items i.e 2 in dict1
# duplicate value are not support instead old value will be replace with new value
dict2 = {
    "name": "Monik", 
    "name": "Bipul",
    "age": 23
    }
print(dict2)

# using dict() constructor
dictConstructor = dict(
    name = "hello",
    age = 101,
    address = "world"
)
print(dictConstructor)
