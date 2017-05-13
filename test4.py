#Найти произведение нечетных цифр пятизначного целого числа, введенного пользователем с клавиатуры
def mul_odd (number):
    lst = [int(x) for x in number if int(x)%2!=0]
    mul = 1
    for i in range (0,len(lst)):
        mul *= lst[i]
    return mul

number = ''
while len(number)!=5:
    number = input("Enter five-digit integer")
print("Multiplication of odd numbers =", mul_odd (number))