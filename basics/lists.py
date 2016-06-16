# collection time complexity https://wiki.python.org/moin/TimeComplexity

import copy

colors = ['red', 'blue', 'green']
# access element
print(colors[0])
# length
print(len(colors))
# assign reference
ref = colors
# shallow copy
copy_shallow_1 = list(colors);
copy_shallow_2 = copy.copy(colors);
copy_shallow_3 = colors[:]
# deep copy
copy_deep = copy.deepcopy(colors)
# concatenation
print([1, 2] + [3, 4])
# for var in list, Do not add or remove from the list during iteration
squares = [1, 4, 9, 16]
sum = 0
for num in squares:
    sum += num
print(sum)
# value in collection
if "red" in colors:
    print("red")

# 0, 1, ... n-1
r1 = range(6)
# a, a+1, ... b-1
r2 = range(3, 9)

list = ['larry', 'curly', 'moe']
list.insert(0, 'xxx')
list.append('shemp')
# add multiple to end of list
list.extend(['yyy', 'zzz'])
# search and return index
list.index('curly')
# pop ith element
list.pop(1)
# search and remove
list.remove('curly')
# remove last two elements
del list[-2:]
print(list)

# remove varibale definition
del list


# list comprehension [ expr for var in list ]
nums = range(1, 4)
squares = [n * n for n in nums]
print(squares)

# combining with if statement
fruits = ['apple', 'cherry', 'bannana', 'lemon']
print([s.upper() for s in fruits if 'a' in s])