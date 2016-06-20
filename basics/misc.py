# 1. else to check calling of break inside while and for loop
numbers = [1, 3, 5]
position = 0
while position < len(numbers):
    if numbers[position] % 2 == 0:
        print("even number, break")
        break
    position += 1
else:
    print('break not called')

numbers = [1, 2, 5]
for num in numbers:
    if num % 2 == 0:
        print("even number, break")
        break
else:
    print('break not called')

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

# 3. generators
generator = (number for number in range(1, 6))
print(type(generator))


