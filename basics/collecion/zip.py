# 2. iterate multiple sequences
# zip() stops when the shortest sequence is done
days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach', 'mango']

for d, f in zip(days, fruits):
    print(d, "-", f)

# use zip to create dict and tuple list
tuple_list = list(zip(days, fruits))
dict = dict(zip(days, fruits))

print(tuple_list)
print(dict)