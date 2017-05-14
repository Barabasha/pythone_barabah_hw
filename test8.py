# В одномерном массиве поменять местами минимальный и максимальный элементы. Остальные оставить на своих местах.
import random
lst=[]
n=10
lower_limit = 0
upper_limit = 100

lst = [random.randint(lower_limit, upper_limit) for x in range(n)]
print (lst)

max_idx = lst.index(max(lst))
min_idx = lst.index(min(lst))

lst[max_idx], lst[min_idx] = lst[min_idx], lst[max_idx]
print(lst)



