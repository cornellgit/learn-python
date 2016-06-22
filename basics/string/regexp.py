# reference see https://developers.google.com/edu/python/regular-expressions

import re

# 1. re.search(pat, str)
str = 'an example word:cat!!'
# r means raw, recommended
match = re.search(r'word:\w\w\w', str)
if match:
    print(match.group())
else:
    print('not found')

# + means 1 or more
# * means 0 or more
# ? means 0 or 1
# [] indicate a set of chars
match = re.search(r'[\w.-]+@[\w.-]+', 'purple alice-b@google.com monkey dishwasher')
print(match.group())

# ( ) group feature
match = re.search(r'([\w.-]+)@([\w.-]+)', 'purple alice-b@google.com monkey dishwasher')
print(match.group())
print(match.group(1))
print(match.group(2))

# find all
# strings = re.findall(r'some pattern', f.read())
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
emails = re.findall(r'[\w\.-]+@[\w\.-]+', str)
for e in emails:
    print(e)

# findall and Groups
tuples = re.findall(r'([\w\.-]+)@([\w\.-]+)', str)
for t in tuples:
    print(t[0])
    print(t[1])

# paren ( ) groupings in the pattern but which you do not want to extract.
# e.g. (?: ) and that left paren will not count as a group result
# .*? .+? forces the greedy match to be non-greedy


# re.sub(pat, replacement, str) substitution
print(re.sub(r'([\w\.-]+)@([\w\.-]+)', r'\1@domain.com', str))
