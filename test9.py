# Нормировать одномерный массив случайных чисел. Нормирование означает приведение всех значений массива к интервалу [-1;1],
# причем максимальное абсолютное значение элементов после нормирование должно быть равно 1.
# Например, последовательность {-5, 3, 4} после нормирование будет выглядеть {-1, 0.6, 0.8}
import random
lst=[]
n=3
lower_limit = -10
upper_limit = 10

for i in range(n):
    lst.append(random.randint(lower_limit,upper_limit))
lst.sort()
print (lst)

max_abs = lst [0]
for i in range(n-1):
    if abs(lst[i+1]) > abs(max_abs):
        max_abs = lst[i+1]

for i in range(n):
    lst[i] /= abs(max_abs)
print(lst)



