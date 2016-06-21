# 1. use exception
def divide(x, y):
    try:
        res = x / y
    # except: means catch all
    except ZeroDivisionError as err:
        print(err)
    else:
        print('result:', res)
    finally:
        print('x:%d,y:%d' % (x, y))


divide(1, 2)
divide(2, 0)


# 2. customized exception
# exception is a class. It is a child of the class Exception
class MyException(Exception):
    pass
    # pass means letting its parent class Exception figure out


try:
    raise MyException("my exception msg")
except MyException as err:
    print(err)
