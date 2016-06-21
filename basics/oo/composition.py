# use class in another class


class ComponentA:
    def __init__(self, val):
        self.val = val


class ComponentB:
    def __init__(self, val):
        self.val = val


class Composite:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return str(type(self.a)) + self.a.val + str(type(self.b)) + self.b.val


print(Composite(ComponentA(' 0 '), ComponentB(' 1 ')))
