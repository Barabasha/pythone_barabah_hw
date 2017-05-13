#Создать программу, выводящую на экран ближайшее к 10 из двух чисел, введенных пользователем.
def near(a,b):
    if abs(10-a)<abs(10-b):
        return a
    elif abs(10-a)>abs(10-b):
        return b
    else:
        return 'Distances equal'

a = float(input("Enter the first number"))
b = float(input("Enter the second number"))
print(near(a,b))

