empty_set = set()
char_set = set('words')
print(char_set)

# & .intersection, notice empty set is considered false
set1 = {'a', 'b', 'c'}
set2 = {'c', 'd', 'e'}
print(set1 & set2)

# | .union
print(set1 | set2)

# - for .difference
print(set1 & set2)

# ^ .symmetric_difference ,xor item in one set not the other
print(set1 ^ set2)

# <= .issubset, < for proper subset
if set1 <= set2:
    print("is subset")


# .issuperset, > proper superset
if set1 >= set2:
    print("is superset")
