

class Human(object):
    def __init__(self, age):
        self.age = age


class Male(Human):
    sex = 'M'

class Famale(Human):
    sex = 'F'


class GridFirend(Famale):
    def __init__(self, age=None):
        self.face = {
            'color': '#FDF1DF',
            'level': 'beautiful',
        }
        self.hair = {
            'color': 'black',
            'level': 'long',
            'style': 'no tangtou',
        }
        self.age = age or 16
        self.high = '165cm'
        self.cup = 'C'
