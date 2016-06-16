import random

nums = []
# 1. generate pseudo random integer
for i in range(5):
    nums.append(random.randrange(100))
print(nums)

# 2. return a new sorted list
l = sorted(nums, reverse=True)

# .sort function changes the original list
# + can be a bit faster than sorted
# - does not work on any enumerable collection
nums.sort(reverse=True)
print(nums)

# 3. key function transforms before comparison
strs = ['ccC', 'AA', 'd', 'bb']
# e.g. sort by string length
print(sorted(strs, key=len))
# sort by lower case
print(sorted(strs, key=str.lower))


