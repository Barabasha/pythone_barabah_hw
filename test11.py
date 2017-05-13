#В двумерном массиве отсортировать четные столбцы по возрастанию, а нечетные - по убыванию

def random_table(table):
    import random
    for idx1 in range(line):
        for idx2 in range(column):
            table[idx1][idx2] = random.randint(1,100)
    return table

def print_table(table):
    for line in table:
        for elem in line:
            print(elem, end="\t")
        print()
    return

def my_sort (table):
    for i in range(column):
        s = []
        for j in range(line):
            s.append(table[j][i])
        if i%2 == 0:
            s.sort(reverse=True)
        else:
            s.sort()
        for j in range(line):
            table[j][i] = s[j]
    return table

line = 3
column = 8
lst = [[0]*column for i in range(line)]
random_table(lst)
print_table(lst)
print()
my_sort(lst)
print_table(lst)

