def max_numeral ():
    import random
    number = random.randint (100000000000,999999999999)
    print("Number", number)
    number = str(number)
    max = int(number [0])
    for i in range (1,12):
        if int(number[i])>max:
            max = int(number[i])
    return max

print ("max of number", max_numeral())


