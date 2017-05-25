# Создать два класса: Окружность и Точка.
# Создать в классе окружности метод, который принимает в качестве параметра точку
# и проверяет находится ли данная точка внутри окружности.

import circle
import point

if __name__ == "__main__":
    my_circle = circle.Circle(0,0,5)
    my_point = point.Point (6,5)
    my_circle.print_info()
    my_point.print_info ()

if my_circle.is_point_in_circle(my_point) == True:
    print ("The point is in a circle")
else :
    print("The point is not in a circle")
