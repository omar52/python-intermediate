# sets is a collection of data type that is unordered, unindexed, and unchangeableunmutable
# it does not allow duplicates

# sets syntax
mySet = {1, 2, 3, 4, 5, 5}
print(type(mySet))  # <class 'set'>
print(mySet)  # {1, 2, 3, 4, 5}  as it does not allow duplication

# creating a set using set() method
mySet2 = set([1, 2, 3, 4, 5, 5])
print(type(mySet2))  # <class 'set'>
print(mySet2)  # {1, 2, 3, 4, 5}  as it does not allow duplication

# proof that set is unordered
mySet3 = set("ommar")
print(mySet3)  # {'o', 'm', 'a', 'r'}  as it does not allow duplication

# as sets do not allow duplicates, we can use it to define how many different character in my word

# creating eMpty set
mySet4 = set()
print(type(mySet4))  # <class 'set'>

# SET ADDING ELEMENTS
mySet5 = {1, 2, 3}
# 1- USINHG ADD METHOD
mySet5.add(4)
print(mySet5)  # {1, 2, 3, 4}

# 2- USING UPDATE METHOD
mySet5.update([5, 6, 7])
print(mySet5)  # {1, 2, 3, 4, 5, 6, 7}
# 3- USING UPDATE METHOD WITH DICTIONARY
mySet5.update({8: 9})
print(mySet5)  # {1, 2, 3, 4, 5, 6, 7, 8}

# SET DELETING ELEMENTS
#1- USING REMOVE METHOD : DELETE IF THE ELEMENT IS EXISTED, IF NOT IT ARISE AN ARROR
mySet5.remove(3)
print(mySet5)  # {1, 2, 3, 4, 5, 6, 7}
# 2- USING DISCARD METHOD : DELETE IF THE ELEMENT IS EXISTED, IF NOT IT DOES NOT ARISE AN ARROR
mySet5.discard(8)
print(mySet5)  # {1, 2, 3, 4, 5, 6, 7}
# 3- USING POP METHOD : DELETE an arbitary element
# it does not take any parameter
print(mySet5.pop())  # 1
print(mySet5)  # {2, 3, 4, 5, 6, 7}


# looping through a set
mySet6 = {1, 2, 3, 4, 5}
# 1- USING FOR-in LOOP
for i in mySet6:
    print(i)  # 1 2 3 4 5
    
    
# checking if an item is in a set
mySet7 = {1, 2, 3, 4, 5}
print(1 in mySet7)  # True
print(6 in mySet7)  # False

# operation on sets {unions, intersection, difference, symmetric difference}
# 1- UNION  
mySet8 = {1, 2, 3}
mySet9 = {3, 4, 5}  
mySet10 = mySet8.union(mySet9)
print(mySet10)  # {1, 2, 3, 4, 5}
# 2- INTERSECTION   
a = {1, 2, 3}
b = {3, 4, 5}
c = a.intersection(b)
print(c)  # {3}
# 3- INTERSECTION UPDATE
a = {1, 2, 3}
b = {3, 4, 5}
a.intersection_update(b)    
print(a)  # {3}  # a is updated to the intersection of a and b
# 3- DIFFERENCE
a = {1, 2, 3}
b = {3, 4, 5}
c = a.difference(b)
print(c)  # {1, 2}  
#4- DIFFERENCE UPDATE
a = {1, 2, 3}
b = {3, 4, 5}
a.difference_update(b)
print(a)  # {1, 2}  # a is updated to the difference of a and b
# 4- SYMMETRIC DIFFERENCE  : all element except the intersection result
a = {1, 2, 3}
b = {3, 4, 5}
c = a.symmetric_difference(b)
print(c)  # {1, 2, 4, 5}
# 5- SUBSET
a = {1, 2, 3}
b = {1, 2, 3, 4, 5}
print(a.issubset(b))  # True    
# 6- SUPERSET
a = {1, 2, 3}
b = {1, 2, 3, 4, 5}
print(b.issuperset(a))  # True
# 7- DISJOINT SETS
a = {1, 2, 3}
b = {4, 5, 6}
print(a.isdisjoint(b))  # True
# 8- CLEAR
a = {1, 2, 3}
b = {4, 5, 6}
a.clear()  # clear the set
print(a)  # set()  # empty set

# 7- FROZEN SET
# frozen set is a set that is unchangeable
myFrozenSet = frozenset([1, 2, 3, 4, 5])
print(type(myFrozenSet))  # <class 'frozenset'>
# myFrozenSet.add(6)  # AttributeError: 'frozenset' object has no attribute 'add'
# myFrozenSet.remove(1)  # AttributeError: 'frozenset' object has no attribute 'remove'


# copy of set
mySet11 = {1, 2, 3}
mySet12 = mySet11.copy()  # create a copy of the set
print(mySet12)  # {1, 2, 3} 
# if we change the original set, the copy will not be affected
mySet12.add(4)  # add 4 to the copy 
print(mySet11)  # {1, 2, 3}
print(mySet12)  # {1, 2, 3, 4}