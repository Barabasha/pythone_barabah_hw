#Создать массив из 10 элементов и проинициализировать его простыми числами в случайном порядке
def my_shuffle (lst):
    import random
    for i in range(0,len(lst)-1):
        r = random.randint(i+1,len(lst)-1)
        x = lst[i]
        lst[i] = lst[r]
        lst[r] = x
    return lst

def prime (lst):
    import math
    lst.append(2)
    for x in range (3,100):
        prime_found = True
        for y in range (2,int(math.sqrt(x)+1)):
            if x%y == 0 :
                prime_found = False
                break
        if prime_found == True:
            lst.append(x)
    return lst

lst = []
prime_number = []
prime_number=my_shuffle(prime(lst))
for i in range(0,10):
    print(prime_number[i],end = "\t")


