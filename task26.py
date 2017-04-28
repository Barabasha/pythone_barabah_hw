def create_list(num, lower_limit, upper_limit):
    import random
    lst = []
    for i in range(num):
        lst.append(random.randint(lower_limit, upper_limit))
    return lst

def even_odd (lst):
    sum_even = 0
    sum_odd = 0
    for elem in lst:
        if elem%2 == 0:
            sum_even += elem
        else:
            sum_odd += elem
    return sum_even - sum_odd

lst = create_list(10, 0, 100)
print(lst)
print(even_odd(lst))
