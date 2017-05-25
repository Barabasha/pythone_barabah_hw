class Godzila:
    stomach = None
    amount_eaten = 0
    limit = None

    def is_hungry(self, food):
        full = 100
        fullness = (self.amount_eaten + food) * full / self.stomach
        if fullness < self.limit:
            self.amount_eaten += food
            print("I ate :", food, "The stomach is full on :", fullness, "%" )
            return False
        else:
            print("I ate : %.2f That's enough. The stomach is full on : %.2f " %(fullness - self.limit, self.limit))
            return True

    def __init__(self,stomach,amount_eaten,limit):
        self.stomach = stomach
        self.amount_eaten = amount_eaten
        self.limit = limit

import random
our_godz = Godzila(1000,0,90)
food = 0
while our_godz.is_hungry(food) == False:
    food = random.randint (20,150)








