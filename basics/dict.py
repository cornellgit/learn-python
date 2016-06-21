# 1.1 initialization, empty dict {}
dict = {}
dict['a'] = 'alpha'
dict['g'] = 'gamma'
dict['o'] = 'omega'
# more succinct
dict = {'a': 'alpha', 'g': 'gamma', 'o': 'omega'}

# 1.2 access missing key
if 'a' in dict:
    print('found ' + dict.get('a'))

dict.setdefault('not_exist_key', '0')

# 1.3 default dict
from collections import defaultdict
food_counter = defaultdict(int)
for food in ['spam', 'spam', 'eggs', 'spam']:
    food_counter[food] += 1

print(food_counter)


# 2. dict comprehension, reverse key and value
dict_rev = {desc: ch for ch, desc in dict.items()}
print(dict_rev)


# 3. keys and values, and k-v pairs
print(dict.keys())
print(dict.values())
print(dict.items())

# 4. loop through
for k, v in dict.items():
    print(k + '->' + v)

# iterkeys(), itervalues() and iteritems() which avoid the cost of constructing the whole list
# 5. string format
hash = {'word': 'garfield', 'count': 42}
print('I want %(count)d copies of %(word)s' % hash)

# 6. remove
del hash['word']
print(hash)