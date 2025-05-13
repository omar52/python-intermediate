# list: is a mutable collection of data type that is ordered and allow duplicates
myList =["apple", "banana", "cherry"]
# print(myList)

# new empty list creation:
myList2 = ["apple", True, 1 ,2 ,"apple"]  # acceot different data types and also duplicates
print(myList2)

# accsessing elements  from the list
item1 = myList[0]    # first element
print(item1)  # apple
item2 = myList[1]    # second element   
item3 = myList[-1]  
print(item3)  # cherry
item4 = myList[-2]  # second last element

# check if the element is in the list
if "apple" in myList:
    print("yes, apple is in the list")
else:
    print("no, apple is not in the list")

# print("apple" in myList)  # True

myList =["apple", "banana", "cherry"]

# list Methods:
## adding elements to the list
# extend: add items from another list to the end of the list
myList =["apple", "banana", "cherry"]
myList2 =["orange", "kiwi", "mango"]
myList.extend(myList2)  # add items from myList2 to the end of myList
print(myList)  # ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango']
# append: add an item to the end of the list
myList.append("orange")
print(myList)  # ['apple', 'banana', 'cherry', 'orange']
# insert: add an item at a specific position
myList.insert(1, "orange")  # add orange at index 1
print(myList)  # ['apple', 'orange', 'banana', 'cherry', 'orange']

## remove: remove an item from the list
myList.remove("banana")  # remove first occurrence of banana
print(myList)  # ['apple', 'orange', 'cherry', 'orange']
# pop: remove an item at a specific position and return it
item = myList.pop(1)  # remove item at index 1
print(item)  # orange
print(myList)  # ['apple', 'cherry', 'orange']
# clear: remove all items from the list
myList.clear()  # remove all items
print(myList)  # []

# reverse: reverse the order of the list
myList =["apple", "banana", "Zebra","cherry"]
myList.reverse()  # reverse the order of the list
print(myList)  # ['cherry', 'Zebra', 'banana', 'apple']

# sort: sort the list in ascending order
myList.sort()  # sort the list in ascending order, as it sorts the uppercase firstfirst.
# the previous command will change the list itself, to avpid this we can use
newList = sorted(myList, key=str.lower)  # sort the list in ascending order
print(newList) # ['apple', 'banana', 'cherry', 'Zebra']
print(myList)  # ['Zebra', 'apple', 'banana', 'cherry']

# join: join the items of the list into a string
myList =["apple", "banana", "cherry"]
myString = ", ".join(myList)  # join the items of the list into a string
print(myString)  # apple, banana, cherry

# split: split a string into a list
myString = "apple, banana, cherry"
myList = myString.split(", ")  # split the string into a list  or list(myString.split(", "))
print(myList)  # ['apple', 'banana', 'cherry']

name = "Omar abdou elsayed"
nameList = name.split(" ")  # split the string into a list
print(nameList)  # ['Omar', 'abdou', 'elsayed'] 

firstList = list(name[0:4])
print(firstList)  # ['O', 'm', 'a', 'r']

# count: return the number of times an item appears in the list
myList =["apple", "banana", "cherry", "apple"]
count = myList.count("apple")  # count the number of times apple appears in the list
print(count)  # 2

#copy: create a copy of the list
myList =["apple", "banana", "cherry"]
myList2 = myList.copy()  # create a copy of the list
print(myList2)  # ['apple', 'banana', 'cherry']
# if we change the original list, the copy will not be affected,but if we change the copy, the original list will not be affected
myList2[0] = "orange"  # change the first element of the copy
print(myList)  # ['apple', 'banana', 'cherry']
print(myList2)  # ['orange', 'banana', 'cherry']
# easy way to create a list:
myList = [0] * 5  # create a list of 5 zeros
print(myList)  # [0, 0, 0, 0, 0]
myList2 = [1,2,3,4,5,6,7,8,9,10]
newList = myList + myList2  # concatenate two lists
print(newList)  # [0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# anothe easy way to create a list:
myList = list(range(0, 11))  # create a list of numbers from 0 to 10
print(myList)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# list comprehension: create a list using a for loop
myList = [x for x in range(0, 11)]  # create a list of numbers from 0 to 10
print(myList)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#slicing: create a new list from an existing list
myList = [1,2,3,4,5,6,7,8,9,10]
newList = myList[0:5]  # create a new list from index 0 to 4
print(newList)  # [1, 2, 3, 4, 5]

# Tricky way to slice a list:
myList = [1,2,3,4,5,6,7,8,9,10]
newList = myList[::2]  # create a new list from index 0 to 4
print(newList)  # [1, 3, 5, 7, 9]

# creatin a list with squaed numbers:
myList = [x**2 for x in range(0, 11)]  # create a list of squared numbers from 0 to 10
print(myList)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# list of strings:
myList = ["apple", "banana", "cherry"]
print(myList)  # ['apple', 'banana', 'cherry']
# access the elements of the list
item = myList[0]  # access the first element
print(item)  # apple

# list of lists:
myList = [[1,2,3],[4,5,6],[7,8,9]]
print(myList)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# access the elements of the list of lists
item = myList[0][1]  # access the first list and the second element
print(item)  # 2

# list of tuples:
myList = [(1,2,3),(4,5,6),(7,8,9)]
print(myList)  # [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
# access the elements of the list of tuples
item = myList[0][1]  # access the first tuple and the second element
print(item)  # 2