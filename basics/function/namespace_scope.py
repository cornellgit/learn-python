#  namespaces—sections within which a particular name is unique

var = 'val_1'


# 1. global scope
def change_n_print_global():
    global var
    var = 'val_2'
    print('changing value:', var, id(var))
    print(locals())


# notice global value id change also, because the string is immutable
# this is new to java, enable string to modify a global immutable object
print('before change:', var, id(var))
change_n_print_global()
print('after change:', var, id(var))

# 2. local scope

var = 'val_1'


def change_n_print_local():
    var = 'val_2'
    print('changing value:', var, id(var))
    print(locals())


print('before change:', var, id(var))
change_n_print_local()
print('after change:', var, id(var))

# 3. get local and global variables as dict, #contents of the local/global namespace.
print(globals())


# 4. __ is used for Python only, e.g. __main__ for main function reference
def dunder():
    """This is a documentation of dunder"""
    print('function name:', dunder.__name__)
    print('doc string:', dunder.__doc__)

dunder()