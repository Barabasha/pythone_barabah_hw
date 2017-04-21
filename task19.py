# Не совсем понял, что значит числа, которые являются степенью 3ки, поэтому даю два варианта
# Вариант sum = 0^3 + 1^3 + 2^3 + ......
x = 0
sum = 0
while pow(x,3) <= 1000001 :
    number = pow(x,3)
    sum = sum + number
    print(x, number)
    x = x + 1
print("Сумма всех чисел в третьей степени =", sum)

# Вариант sum = 3^0 + 3^1 + 3^2 + ......
n = 0
sum = 0
while pow(3,n) <= 1000001 :
    number = pow(3,n)
    sum = sum + number
    print(n, number)
    n = n + 1
print("Сумма всех троек в степени n =", sum)


