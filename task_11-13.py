def print_task(n) :
    print ('====================Task'+str(n)+'====================')
    return

#==================task11==================
import math
print_task(11)

def degree2radian (deg):
    rad = deg *  math.pi / 180
    return rad

print("cos of 60 degrees =",math.cos(degree2radian (60)))
print("cos of 45 degrees =",math.cos(degree2radian (45)))
print("cos of 40 degrees =",math.cos(degree2radian (40)))
print()

#==================task12==================
print_task(12)

def num2sum (number):
    num1 = int (number / 100) #find the first digits
    num2 = int ((number - num1*100)/10) #find the second digits
    num3 = number - num1*100 - num2*10
    sum = num1 + num2 + num3
    return sum

number = int(input('Input number: '))
print("Sum of digits of number", number, "=", num2sum (number))
print()

#==================task13==================
def square (a,b):
    square = a * b / 2
    return square

def perimeter (a,b):
    per = a + b + math.sqrt(pow(a,2) + pow(b,2))
    return per

print_task(13)
lenght_a = int(input("Input the first cathetus = "))
lenght_b = int(input("Input the second cathetus = "))
print('Square of triangl =', square(lenght_a, lenght_b))
print('Perimetr of triangl =', perimeter(lenght_a, lenght_b))


