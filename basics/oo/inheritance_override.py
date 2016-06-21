# 0. a simple super class
class Person:
    def __init__(self, name):
        self.name = name

    def say_sth(self):
        print(self.name, " Person, super-class")


# 1. inheritance and override
class Engineer(Person):
    # delegate to super class for initialization
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email

    # override function
    def say_sth(self):
        print(self.name, " Engineer, a sub-class")


eng = Engineer("Mary", "mary@google.com")
eng.say_sth()





# empty class
class Empty:
    pass
