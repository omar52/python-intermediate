# itertools: product, permutations, combinations, accumulate, groupby, infinite iterators 

# itertools is a module in Python that provides functions that create iterators for efficient looping.
# It includes functions for creating iterators for looping over data, such as product, permutations, combinations, and more.

from itertools import product, permutations, combinations, accumulate, groupby, count, cycle, repeat

# 1. product: Cartesian product of input iterables
# The product() function returns the Cartesian product of input iterables.
# It takes one or more iterables as arguments and returns an iterator that produces tuples of all possible combinations of the input iterables.
# Example:
a = [1, 2]
b = [3, 4]
result = product(a, b, )
print("Product:" , list(result))
# Output: [(1, 3), (1, 4), (2, 3), (2, 4)]

# 2. permutations: All possible orderings of input iterable
# The permutations() function returns all possible orderings of the input iterable.
# It takes an iterable as an argument and returns an iterator that produces tuples of all possible orderings of the input iterable.
# Example:
a = [1, 2, 3]
result = permutations(a)
print("Permutations:" , list(result))
# Output: [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

# 3. combinations: All possible combinations of input iterable
# The combinations() function returns all possible combinations of the input iterable.
# It takes an iterable and a length as arguments and returns an iterator that produces tuples of all possible combinations of the input iterable of the specified length.
# Example:
a = [1, 2, 3]
result = combinations(a, 2)
print("Combinations:" , list(result))
# Output: [(1, 2), (1, 3), (2, 3)]
# example with string
a = 'abc'
result = combinations(a, 2)
print("Combinations:" , list(result))
# Output: [('a', 'b'), ('a', 'c'), ('b', 'c')]

# 4. accumulate: Cumulative sum of input iterable
# The accumulate() function returns the cumulative sum of the input iterable.   
# It takes an iterable as an argument and returns an iterator that produces the cumulative sum of the input iterable.
# Example:
a = [1, 2, 3, 4]
result = accumulate(a)
print("Accumulate:" , list(result))
# Output: [1, 3, 6, 10]
# example with string
a = 'abc'
result = accumulate(a)
print("Accumulate:" , list(result))
# Output: ['a', 'ab', 'abc']

# 5. groupby: Group input iterable by key
# The groupby() function groups the input iterable by key.
# It takes an iterable and a key function as arguments and returns an iterator that produces tuples of the key and the group of items in the input iterable that have that key.
# Example:
persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25}, 
           {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28}]

for key, group in groupby(persons, key=lambda x: x['age']):
    print(key, list(group))

# 6. infinite iterators: count, cycle, repeat
# The count() function returns an iterator that produces an infinite sequence of numbers, starting from a specified number.
# It takes a start number and an optional step as arguments and returns an iterator that produces an infinite sequence of numbers.
# Example:
result = count(1, 2)
print("Count:" , [next(result) for _ in range(5)]) # Output: [1, 3, 5, 7, 9]
# The cycle() function returns an iterator that produces an infinite sequence of items from the input iterable.
# It takes an iterable as an argument and returns an iterator that produces an infinite sequence of items from the input iterable.
# Example:
a = [1, 2, 3]
result = cycle(a)
print("Cycle:" , [next(result) for _ in range(5)]) # Output: [1, 2, 3, 1, 2]
# The repeat() function returns an iterator that produces an infinite sequence of the specified item.
# It takes an item and an optional number of times to repeat as arguments and returns an iterator that produces an infinite sequence of the specified item.
# Example:
result = repeat(1, 5)
print("Repeat:" , list(result)) # Output: [1, 1, 1, 1, 1]

