# arguments are passed by assignment in Python. Since assignment just creates references to objects
# by reference can be achieved,  by returning a tuple of the results


def menu(wine, entree='rice'):
    return {'wine': wine, 'entree': entree}


# 1. positional ref vs. keyword argument, vs mixture
print(menu('red', 'beef'))
print(menu(wine='red', entree='beef'))
# in case of mix, positional ref need to come first
print(menu('red', entree='beef'))

# 2. default parameter
# careful of using [] as default, it'll be reused
print(menu('red'))


# 3.1 * groups positional arguments into tuple
def print_args(*args):
    print(args)


print_args()
print_args(1, 2, 'third')


# 3.2 * groups keyword arguments into dict

def print_kwargs(**kwargs):
    print('Keyword arguments:', kwargs)


print_kwargs()
print_kwargs(k1="key 1", k2=2)
