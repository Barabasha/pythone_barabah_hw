def guess_number(x):
    if x < 1 or x > 10:
        print("Enter the correct number")
    elif x < number:
        print("Your number is less")
    elif x > number:
        print("Your number is greater")

import random
number = random.randint(1,10)
x = 0
while x!=number:
    x = int(input("Enter number from 1 to 10"))
    guess_number(x)
print ("Bravo!")




