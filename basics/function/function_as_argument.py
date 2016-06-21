# function is an object
# 5.1 Use function as a parameter to another function
def run_function(func, *args):
    return func(*args)


def sum_all(*args):
    return sum(args)


print(run_function(sum_all, 1, 2, 3, 4))


# 5.2 Anonymous Functions: the lambda(), it's optional, I can always replace it with 5.1
# lambda argument1, argument2,... argumentN : expression using arguments
# lambda function is an anonymous function expressed as a single statement
def word_transform(words, func):
    for w in words:
        print(func(w))


word_transform(['thud', 'meow', 'thud', 'hiss'], lambda w: w.upper())
# another example
f = lambda x, y, z: x + y + z
print(f(1, 2, 3))
