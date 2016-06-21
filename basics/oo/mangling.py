#  name mangling to create a private variable, not truly

class GetSet:
    def __init__(self, input_nm):
        self.__name = input_nm

    @property
    def name(self):
        print("getter method")
        return self.__name

    @name.setter
    def name(self, input_nm):
        print("setter method")
        self.__name = input_nm


gs = GetSet('Mary')
gs.name = 'mary'
gs.name
# private cannot be accessed, gs.__name
# access by gs._GetSet__name


