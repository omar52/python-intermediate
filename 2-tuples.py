# tUPLE: Imutable, ordered collection of items and allows duplicates
# tuple must have at least one item and a comma
myTuple = ("omar")
print(type(myTuple))  # <class 'str'>
myTuple = ("omar",) # add a comma to make it a tuple
print(type(myTuple))  # <class 'tuple'>

# we can use tuple general function to create a tuple
myTuple = tuple(["omar", 28, "Sinai"])
print(myTuple)  # ('omar', 28, 'Sinai')

# accessing tuple items
myTuple = ("omar", 28, "Sinai")
print(myTuple[0])  # omar
print(myTuple[1])  # 28 
print(myTuple[2])  # Sinai
print(myTuple[-1])  # Sinai
print(myTuple[-2])  # 28
print(myTuple[-3])  # omar
print(myTuple[0:2])  # ('omar', 28)
print(myTuple[0:3])  # ('omar', 28, 'Sinai')

# check if tuple is immutable:
myTuple = ("omar", 28, "Sinai")
# myTuple[0] = "ahmed"  # TypeError: 'tuple' object does not support item assignment

# iteration over tuple
myTuple = ("omar", 28, "Sinai")
for item in myTuple:
    print(item)  # omar 28 Sinai 
    
# check if an item exists in tuple
myTuple = ("omar", 28, "Sinai")
print("omar" in myTuple)  # True
print("ahmed" in myTuple)  # False

# methods of tuple
myTuple = ("omar", 28, "Sinai")
print(myTuple.count("omar"))  # 1
print(myTuple.count("ahmed"))  # 0
print(myTuple.index("omar"))  # 0
print(myTuple.index("Sinai"))  # 2
# print(myTuple.index("ahmed"))  # ValueError: 'ahmed' is not in tuple
len(myTuple)  # 3
#Tuple slicing
myTuple = (0,1,2,3,4,5,6,7,8,9)
print(myTuple[0:5])  # (0, 1, 2, 3, 4)
# slicing with step
print(myTuple[:10:2])  # (0, 2, 4, 6, 8)

# unpacking tuple
myTuple = ("omar", 28, "Sinai")
name, age, city = myTuple
print(name)  # omar
print(age)  # 28   
print(city)  # Sinai

# unpacking tuple with *
myTuple = ("omar", 28, "Sinai", "Egypt")
name, *rest , country = myTuple
print(name)  # omar
print(rest)  # [28, 'Sinai']  Returned in list form
print(country)  # Egypt    

#  comparison between tuples and lists from number of bytes for the same elements
import sys
myList = [1, 2, 3, 4, 5]
myTuple = (1, 2, 3, 4, 5)
print(sys.getsizeof(myList), "pytes")  # 104
print(sys.getsizeof(myTuple), "pytes")  # 56

# another comparison from time of creation
import timeit
print(timeit.timeit(stmt="[0 ,1, 2, 3, 4, 5]", number=1000000))  # 0.1267764000222087
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))  # 0.045536199992056936
