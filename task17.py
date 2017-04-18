def print_task(n) :
    print ('====================Task'+str(n)+'====================')
    return

#===========================task17===========================
import math
print_task(17)
print ("ax^2 + bx + c = 0")
a = int(input ("Input value of a"))
b = int(input ("Input value of b"))
c = int(input ("Input value of c"))

def root (a,b,c):
    d = pow(b,2) - 4*a*c
    if a == 0 and b == 0 and c == 0 :
        return 0, 0, 3
    elif a == 0 and b == 0 :
        return 0, 0, 4
    elif a == 0 and c == 0:
        return 0, 0, 1
    elif a == 0 :
        return -c/b, 0, 1
    elif d>0 :
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return x1, x2, 2
    elif d == 0 :
        x1 = -b / (2 * a)
        return x1, x1, 1
    elif d < 0 :
        return 0, 0, 0

x1, x2, roots = root(a,b,c)
if roots == 2 :
    print ("Roots:", x1, x2)
elif roots == 1 :
    print ("Root:", x1)
elif roots ==0 :
    print ("there is not a decision")
elif roots == 3:
    print ("any value")
elif roots == 4:
    print ("not correct equalization")