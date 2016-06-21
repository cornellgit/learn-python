class Str:
    def __init__(self, txt):
        self.txt = txt

    def __eq__(self, other):
        return self.txt.lower() == other.txt.lower()

    def __str__(self):
        return self.txt

    def __repr__(self):
        return self.txt


print(Str('HH') == Str('hh'))
print(Str('HH'))
