class Customer:
    name = ''
    id = ''
    age = 0
    credit = 0
    level = ''

    def __init__(self, name='', age=0, id='', credit=0, level=''):
        self.name = name
        self.age = age
        self.id = id
        self.level = level
        self.credit = credit

    def __str__(self):
        return f'{self.name} {self.age} {self.id} {self.level} {self.credit}'


class Vip(Customer):
        minus = -500


class Premium(Vip):
    minus = -1000