def create_list(num, lower_limit, upper_limit):
    import random
    lst = []
    for i in range(num):
        lst.append(random.randint(lower_limit, upper_limit))
    return lst

def avr_list (lst):
    sum = 0
    for i in range (len(lst)):
        sum = sum + lst[i]
    avr = sum / len(lst)
    return avr

lst = create_list (10,0,100)
if len(lst) == 0:
    print("List is empty")
else:
    print(lst)
    print("Average =", avr_list(lst))