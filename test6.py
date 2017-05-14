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
    for prime_found in range (3,100):
        count = True
        for y in range (2,int(math.sqrt(prime_found)+1)):
            if prime_found%y == 0 :
                count = False
                break
        if count == True:
            lst.append(prime_found)
    return lst

lst = []
prime_number = []
for i in range(0,10):
    prime_number.append(my_shuffle(prime(lst))[i])
print(prime_number)


