#Создать программу, выводящую на экран ближайшее к 10 из двух чисел, введенных пользователем.
def near(a,b,number):
    if abs(number-a)<abs(number-b):
        return a
    elif abs(number-a)>abs(number-b):
        return b
    else:
        return 'Distances equal'

a = float(input("Enter the first number"))
b = float(input("Enter the second number"))
number = 10
print(near(a,b,number))

