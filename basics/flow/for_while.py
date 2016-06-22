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