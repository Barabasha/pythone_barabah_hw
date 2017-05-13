#Найти сумму десяти первых чисел ряда Фибоначчи.
def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else :
        return fib(n-1) + fib(n-2)

sum = 0
for i in range (1,11):
    sum += fib(i)
print(sum)