#===========================task15===========================
def print_task(n) :
    print ('====================Task'+str(n)+'====================')
    return

print_task(15)
import math
x1 = int(input ("Введите координату x центра первой окружности"))
y1 = int(input ("Введите координату y центра первой окружности"))
r1 = int(input ("Введите радиус первой окружности"))
x2 = int(input ("Введите координату x центра второй окружности"))
y2 = int(input ("Введите координату x центра второй окружности"))
r2 = int(input ("Введите радиус второй окружности"))

def intersect_circle (x1, y1, r1, x2, y2, r2):
    r = math.sqrt (pow (x2-x1,2) + pow (y2-y1,2))
    if r==0 and r1==r2 :
        return True
    elif ((r1+r2>=r) and (r1+r>=r2) and (r2+r>=r1)):
        return True
    else:
        return False

if intersect_circle(x1, y1, r1, x2, y2, r2) == True:
    print ("Intersect")
else :
    print ("Not intersect")