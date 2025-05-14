# A lambda function is a small (one line) anonymous function that is defined without a name. 
# A lambda function can take any number of arguments, but can only have one expression. While normal functions are defined using the def keyword, in Python anonymous functions are defined using the lambda keyword.

# lambda arguments: expression

# Example 1
# a lambda function that adds 10 to the input argument
f = lambda x : x+1
# print(f(10)) # 11

f2 = lambda x,y : x*y
# print(f2(3,5)) # 15


# Usage example: Lamdba inside another function

# example:

def func(x):
    return lambda n : n * x

double = func(2)
# print(double(10))

triple = func(3)
# print(triple(30))

# Custom sorting using a lambda function as key parameter

points = [(1, 2), (3, -1), (5, 0), (0, 3), (4, -4)]
sorted_by_y = sorted(points, key = lambda x :x[1])
# print(sorted_by_y) # [(4, -4), (3, -1), (5, 0), (1, 2), (0, 3)]


values = [- 1, -4, -2, -3, 1, 2, 3, 4]
sorted_by_abs = sorted(values, key = lambda x : abs(x))
# print(sorted_by_abs) # [1, 2, -1, -2, 3, -3, 4, -4]
# sorted_by_abs = sorted(values, key = abs)

# Use lambda for map function
# map(func, seq), transforms each element with the function.
a = [1, 2, 3, 4, 5, 6]
b = list(map(lambda x : 2*x,a))    # map(function, iterable)
c = [2*x for x in a]  # list comprehension  
# print(b,c)



# Use lambda for filter function
# filter(func, seq), returns all elements for which func evaluates to True.
a = [1, 2, 3, 4, 5, 6]
b = list(filter(lambda x : x%2 ==0,a)) # filter(function, iterable)
c = [x for x in a if x%2 == 0 ] # list comprehension
# print(b,c)


# reduce
# reduce(func, seq), repeatedly applies the func to the elements and returns a single value.
# func takes 2 arguments.

from functools import reduce
a = [1, 2, 3, 4, 5]
product = reduce(lambda a,b :a*b, a) # 1*2*3*4*5 = 120
print(product) # 120
sum = reduce(lambda a,b :a+b, a) # 1*2*3*4*5 = 120
print(sum) # 15

