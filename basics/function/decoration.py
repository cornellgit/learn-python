# 8. decorator - a function that takes one function as input and returns another function
def exe_log(func):
    """enable logging the execution of a function"""

    # define modified function
    def new_function(*args, **kwargs):
        print('Executing Function:', func.__name__)
        print('Positional Arguments:', args)
        print('Keyword Arguments:', kwargs)
        res = func(*args, **kwargs)
        print('Result:', res)
        return res

    # return the modified function
    return new_function


# 8.1 manual decoration
def add_ints(n1, n2):
    return n1 + n2


dec_add_ints = exe_log(add_ints)
dec_add_ints(2, n2=3)


# 8.2 @decorator_name and multiple decorator
def square_it(func):
    def new_function(*args, **kwargs):
        res = func(*args, **kwargs)
        return res * res

    return new_function


@exe_log
@square_it
def add_ints_deced(n1, n2):
    return n1 + n2


print('Final Result:', add_ints_deced(2, 3))


# decorator order matters, the one closest function definition execute first, even though final result is the same
@square_it
@exe_log
def add_ints_deced(n1, n2):
    return n1 + n2


print('Final Result:', add_ints_deced(2, 3))
