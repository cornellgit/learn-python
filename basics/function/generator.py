# 7. generator, just use yield, for example range is a generator
# enable iteration through sequences without creating and storing the entire sequence in memory at once
def custom_range(start=0, end=10, step=1):
    while start < end:
        yield start
        start += step


custom_range_generator = custom_range(0, 4, 2)

print(type(custom_range))
print(type(custom_range_generator))

for n in custom_range_generator:
    print(n)

# generator type
generator = (number for number in range(1, 6))
print(type(generator))
