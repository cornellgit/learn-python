# empty dict {}
dict = {}
dict['a'] = 'alpha'
dict['g'] = 'gamma'
dict['o'] = 'omega'
# more succinct
dict = {'a': 'alpha', 'g': 'gamma', 'o': 'omega'}

# dict comprehension, reverse key and value
dict_rev = {desc: ch for ch, desc in dict.items()}
print(dict_rev)

# contains key
if 'a' in dict:
    print('found ' + dict.get('a'))

# keys and values, and k-v pairs
print(dict.keys())
print(dict.values())
print(dict.items())

# loop through
for k, v in dict.items():
    print(k + '->' + v)

# iterkeys(), itervalues() and iteritems() which avoid the cost of constructing the whole list
# string format
hash = {'word': 'garfield', 'count': 42}
print('I want %(count)d copies of %(word)s' % hash)

# remove
del hash['word']
print(hash)
