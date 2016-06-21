# Avoid over engineering data structures. Tuples are better than objects
from collections import namedtuple

# named tuple is a subclass of tuples, access values by name (with .name) as well as by position (with [ offset ]
Person = namedtuple('Person', 'name email')
mary = Person('Mary', email='mary@google.com')

# ** means key word arguments
peter = Person(**{'name': 'Peter', 'email': 'peter@google.com'})

# access
print(peter[0], peter[1])
print(peter.name, peter.email)

# named tuple is immutable
peter_at_gmail = peter._replace(email='peter@gmail.com')
print(peter_at_gmail)
