# В одномерном массиве поменять местами минимальный и максимальный элементы. Остальные оставить на своих местах.
import random
lst=[]
n=10
lower_limit = 0
upper_limit = 100

for i in range(n):
    lst.append(random.randint(lower_limit,upper_limit))
print (lst)

min_idx=0
max_idx=0
if max(lst)!= min(lst):
    for i in range(len(lst)):
        if lst[i] == max(lst):
            max_idx = i
        elif lst[i] == min(lst):
            min_idx =  i
else:
    print (lst)

elem = lst[max_idx]
lst[max_idx] = lst[min_idx]
lst[min_idx] = elem
print(lst)



