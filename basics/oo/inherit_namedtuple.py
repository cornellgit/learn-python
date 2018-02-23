from collections import namedtuple

# inherit a namedtuple
class Z(namedtuple('X', 'a b c')):
    def __new__(cls, d, a,b,c):
        self = super(Z, cls).__new__(cls, a,b,c,)
        self.d = d
        return self

z = Z(1,2,3,4)

# contains only a,b,c
print(z)

# contains tuple base class attribute
print(hasattr(z, 'a'))

# contains d as a separate attribute
print(z.d)
