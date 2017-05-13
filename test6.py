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
        count = False
        for y in range (2,int(math.sqrt(x)+1)):
            count = False
            if x%y == 0 :
                break
            else: count = True
        if count == True:
            lst.append(x)
    return lst

lst = []
prime_number = []
for i in range(0,10):
    prime_number.append(my_shuffle(prime(lst))[i])
print(prime_number)


