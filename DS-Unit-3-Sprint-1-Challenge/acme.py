import random

class Product:
    def __init__(self, name=None, price=10, weight=20,flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = random.randint(1000000,9999999)


    def stealability(self):
        s = self.price/self.weight
        message=''
        if s<0.5:
            print('Not so stealable...')
            message = 'Not so stealable...'
        elif (s>=0.5) & (s<1):
            print('Kinda stealable')
            message = 'Kinda stealable'
        else:
            print('Very stealable!')
            message = 'Very stealable!'
        return message

    def explode(self):
        f = self.flammability * self.weight
        message =''
        if f<10:
            print('...fizzle.')
            message = '...fizzle.'
        elif (f>=10) & (f<50):
            print('...boom!')
            message = '...boom!'
        else:
            print('...BABOOM!!!')
            message = '...BABOOM!!!'
        return message


class BoxingGlove(Product):

    def __init__(self,name=None, price=10, weight=10,flammability=0.5):
        super().__init__(name=name, price=price, weight=weight, flammability=flammability)

    def explode(self):
        print("...it's a glove.")

    def punch(self):
        if self.weight<5:
            print('That tickles')
        elif (self.weight>5) & (self.weight<15):
            print('Hey that hurt!')
        else:
            print('OUCH!')
