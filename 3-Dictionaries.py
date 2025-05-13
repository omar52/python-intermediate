# Dictionary is a collection of data type that is ordered, mutable and do not allow duplicates.
# collections of key-value pairs


# Creating a dictionary:
myDict = {
    "name": "Omar",
    "age": 27,
    "city": "Zagazig",
    "isStudent": True,
}
print(myDict)

# we can write dictionary usin dict() method
myDict2 = dict(name="Omar", age=27, city="Zagazig", isStudent=True)
print(myDict2)
# we can also create an empty dictionary
myDict3 = {}
print(myDict3)

# Accessing values elements from the dictionary
item1 = myDict["name"]  # first element
print(item1)  # Omar
item2 = myDict["age"]  # second element
print(item2)  # 27
item3 = myDict["city"]  # third element
print(item3)  # Zagazig
item4 = myDict["isStudent"]  # fourth element
print(item4)  # True

# check if the element is in the dictionary
if "name" in myDict:
    print("yes, name is in the dictionary")
else:
    print("no, name is not in the dictionary")


# Adding new items to the dictionary
myDict["country"] = "Egypt"  # add new item
print(myDict)  # {'name': 'Omar', 'age': 27, 'city': 'Zagazig', 'isStudent': True, 'country': 'Egypt'}

# changing the value of an existing item
myDict["age"] = 28  # change the value of age

# deleting an item from the dictionary
# 1-using del keyword
del myDict["isStudent"]  # delete the item with key isStudent
print(myDict)  # {'name': 'Omar', 'age': 28, 'city': 'Zagazig', 'country': 'Egypt'}
# 2-using pop() method
myDict.pop("age")  # delete the item with key age
print(myDict)  # {'name': 'Omar', 'city': 'Zagazig', 'country': 'Egypt'}
# 3-using popitem() method
myDict.popitem()  # delete the last item
print(myDict)  # {'name': 'Omar', 'city': 'Zagazig'}
# 4-using clear() method
# myDict.clear()  # delete all items

# check if key is inside the dictionary:
# 1-using in keyword
if "name" in myDict:
    print("yes, name is in the dictionary")
else:   
    print("no, name is not in the dictionary")  
# 2-using get() method  
item = myDict.get("name")  # get the value of name
print(item)  # None
# 3-using try and except
try:
    item = myDict["name"]  # get the value of name
    print(item)  # Omar
except:
    print("no, name is not in the dictionary")
# 4-using keys() method
keys = myDict.keys()  # get the keys of the dictionary,
print(keys)  # dict_keys(['name', 'city'])

# loops through the dictionary
# 1-using for-in  loop using keys  
for key in myDict.keys():   # returns a view object that displays a list of all the keys in the dictionary, and we can use list() method to convert it to a list to get list
    # print the key and value
    print(key, myDict[key])  # name Omar, city Zagazig
    
# 2-using for-in loop using values
for value in myDict.values(): # returns a view object that displays a list of all the values in the dictionary, and we can use list() method to convert it to a list to get list
    print(value)  # Omar, Zagazig

# 3-using for-in loop using items
for key, value in myDict.items(): # returns a view object that displays a list of all the key-value pairs in the dictionary, and we can use list() method to convert it to a list to get list of tuples
    print(key + ": " + value)  # name: Omar, city: Zagazig

# copying a dictionary (these ,ethods will create a new dictionary with the same key-value pairs, without reference to the original dictionary)
# 1-using copy() method
myDict4 = myDict.copy()  # copy the dictionary, it will create a new dictionary with the same key-value pairs,without reference to the original dictionary
print(myDict4)  # {'name': 'Omar', 'city': 'Zagazig'}
myDict4["name"] = "Ahmed"  # change the value of name in the copied dictionary
print(myDict4)  # {'name': 'Ahmed', 'city': 'Zagazig'}
print(myDict)  # {'name': 'Omar', 'city': 'Zagazig'}
# 2-using dict() method
myDict5 = dict(myDict)  # copy the dictionary, it will create a new dictionary with the same key-value pairs,without reference to the original dictionary
print(myDict5)  # {'name': 'Omar', 'city': 'Zagazig'}
myDict5["name"] = "Ahmed"  # change the value of name in the copied dictionary
print(myDict5)  # {'name': 'Ahmed', 'city': 'Zagazig'}

# updating a dictionary (if there are any existed keys their value will get updated)
myDict.update({"name": "Atef", "age": 27, "city": "Zagazig", "isStudent": True})  # update the dictionary with new key-value pairs
print(myDict)  # {'name': 'Atef', 'age': 27, 'city': 'Zagazig', 'isStudent': True}

# using numbers as keys
myDict6 = {1: "Omar", 2: "Ahmed", 3: "Ali"}  # create a dictionary with numbers as keys
print(myDict6)  # {1: 'Omar', 2: 'Ahmed', 3: 'Ali'}

# using tuples as keys
myDict7 = {("name", "age"): "Omar", ("city", "country"): "Zagazig"}  # create a dictionary with tuples as keys  
print(myDict7)  # {('name', 'age'): 'Omar', ('city', 'country'): 'Zagazig'}
# accessing the value using tuple as key
item = myDict7[("name", "age")]  # get the value of name and age

