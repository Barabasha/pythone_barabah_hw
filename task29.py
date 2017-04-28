def create_list(num, lower_limit, upper_limit):
    import random
    lst = []
    for i in range(num):
        lst.append(random.randint(lower_limit, upper_limit))
    return lst

lst = create_list(11,-1,1)
print(lst)
count0 = 0
count1 = 0
count2 = 0

for elem in lst:
    if elem == 0:
        count0 += 1
        continue
    elif elem == 1:
        count1 += 1
        continue
    else:
        count2 += 1

if count0 > max(count1, count2):
    print("Число '0' встречается чаще всего:", count0, "раз")
elif count1 > max(count0, count2):
    print("Число '1' встречается чаще всего:", count1, "раз")
elif count2 > max(count0, count1):
    print("Число '-1' встречается чаще всего:", count2, "раз")

