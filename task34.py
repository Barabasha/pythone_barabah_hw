class Godzila:
    stomach = None
    amount_eaten = 0
    limit = None

    def eating_people(self,food):
        full = 100
        if self.amount_eaten*full/self.stomach <= self.limit:
            self.amount_eaten += food
        if self.amount_eaten*full/self.stomach >= self.limit:
            print("That's enough. I'm full")
            self.amount_eaten = self.limit*self.stomach/full
        print("I ate" ,self.amount_eaten)

    def __init__(self,stomach,amount_eaten,limit):
        self.stomach = stomach
        self.amount_eaten = amount_eaten
        self.limit = limit

our_godz = Godzila(1000,0,90)
food = 0
while food != 'q' :
    food = input("Enter amount eat or 'q' for exit")
    if food != 'q':
        our_godz.eating_people(int(food))




