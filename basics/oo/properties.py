#  If you don’t specify a setter property for an attribute, you can’t set it from the outside.
# properties is equivalent to getter setter

class Cycle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2


c = Cycle(2)
print(c.diameter)
c.radius = 4
print(c.diameter)

try:
    c.diameter = 6
except AttributeError as e:
    print(e)
