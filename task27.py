import random
lst = []
for i in range(1,100,2):
    lst.append (i)
print(lst)

for i in range(0,len(lst)-1): #число замен у нас меньше на 1, чем длина строки
    r = random.randint(i+1,len(lst)-1) #выбираем индекс, кроме уже использованных
    x = lst[i] #далее меняем местами
    lst[i] = lst[r]
    lst[r] = x
print(lst)






