def create_list(num, lower_limit, upper_limit):
    import random
    lst = []
    for i in range(num):
        lst.append(random.randint(lower_limit, upper_limit))
    return lst

def avr_list(lst):
    sum = 0
    for elem in lst:
        sum += elem
    return sum/len(lst)


lst1 = create_list(5,0,5)
print("Список№1", lst1)
lst2 = create_list(5,0,5)
print("Список№2",lst2)
if avr_list(lst1) == avr_list(lst2):
    print("Средние арифметические этих списков равны")
elif avr_list(lst1) > avr_list(lst2):
    print("Среднее арифметическое Списка№1 больше")
elif avr_list(lst1) < avr_list(lst2):
    print("Среднее арифметическое Списка№2 больше")



