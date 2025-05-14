# collections (Counter, namedtuple , ORderedDict, defaultdict, deque)

from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

# 1-Counter
# Counter is a subclass of dict that helps count hashable objects
a = "aaaaabbbcccc"
b = Counter(a)
print(b)  # Counter({'a': 5, 'c': 4, 'b': 3})
print(b.most_common(2))  # [('a', 5), ('c', 4)]
print(list(b.elements()))  # ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'c']
print(b.most_common(2)[1][0])  # c
print(b.most_common(2)[1][1])  # 4
print(b['a'])  # 5 

# 2-namedtuple
# namedtuple is a factory function for creating tuple subclasses with named fields
Point = namedtuple('Point', 'x,y')
pt = Point(10, 20)
print(pt)  # Point(x=10, y=20)
print(pt.x , pt.y)  # 10

# 3-OrderedDict
# OrderedDict is a subclass of dict that remembers the order in which items were inserted
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
print(od)  # OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od.keys())  # odict_keys(['a', 'b', 'c'])
print(od.values())  # odict_values([1, 2, 3])
print(od.items())  # odict_items([('a', 1), ('b', 2), ('c', 3)])
print(od['a'])  # 1
print(od['b'])  # 2 
print(od['c'])  # 3
# print(od['d'])  # KeyError: 'd'
print(od.get('d'))  # None
print(od.get('d', 0))  # 0
print(od.popitem())  # ('c', 3)
print(od)  # OrderedDict([('a', 1), ('b', 2)])
print(od.popitem(last=False))  # ('a', 1)
print(od)  # OrderedDict([('b', 2)])
print(od.popitem(last=True))  # ('b', 2)
print(od)  # OrderedDict([])

# 4-defaultdict
# defaultdict is a subclass of dict that returns a default value when a key is not found    
dd = defaultdict(int)
dd['a'] = 1
dd['b'] = 2
dd['c'] = 3
print(dd)  # defaultdict(<class 'int'>, {'a': 1, 'b': 2, 'c': 3})
print(dd['a'])  # 1
print(dd['b'])  # 2
print(dd['c'])  # 3
print(dd['d'])  # 0
print(dd)  # defaultdict(<class 'int'>, {'a': 1, 'b': 2, 'c': 3, 'd': 0})
print(dd['e'])  # 0
print(dd)  # defaultdict(<class 'int'>, {'a': 1, 'b': 2, 'c': 3, 'd': 0, 'e': 0})
print(dd['f'])  # 0
print(dd)  # defaultdict(<class 'int'>, {'a': 1, 'b': 2, 'c': 3, 'd': 0, 'e': 0, 'f': 0})

# 5-deque
# deque is a list-like container with fast appends and pops on either end
d = deque()
d.append(1)
d.append(2) 
d.append(3)
d.appendleft(0)
print(d)  # deque([0, 1, 2, 3])
d.pop()
print(d)  # deque([0, 1, 2])
d.popleft() 
print(d)  # deque([1, 2])
d.extend([4, 5, 6])
print(d)  # deque([1, 2, 4, 5, 6])
d.extendleft([0, -1, -2])   
print(d)  # deque([-2, -1, 0, 1, 2, 4, 5, 6])
d.rotate(2)  # Rotate the deque to the right by 2 steps 
print(d)  # deque([5, 6, -2, -1, 0, 1, 2, 4])
d.rotate(-2)  # Rotate the deque to the left by 2 steps
print(d)  # deque([-2, -1, 0, 1, 2, 4, 5, 6])
d.clear()  # Clear the deque
print(d)  # deque([])