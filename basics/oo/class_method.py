class CountInstance:
    cnt = 0

    # this is instance method
    def __init__(self):
        CountInstance.cnt += 1

    @classmethod
    def get_cnt(cls):
        return cls.cnt

    @staticmethod
    def static_method():
        print('class definition affects neither the class nor its objects')


CountInstance.static_method()

CountInstance()
CountInstance()
print(CountInstance.get_cnt())
