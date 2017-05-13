#Вывести на экран матрицу, транспонированную заданной (3*8)
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

def table_revers(table):
    for idx1 in range(line_reverse):
        for idx2 in range(column):
            elem = table[idx1][idx2]
            table[idx1][idx2] = table[line - idx1 - 1][idx2]
            table[line - idx1 - 1][idx2] = elem
    for idx1 in range(line):
        for idx2 in range(column_reverse):
            elem = table[idx1][idx2]
            table[idx1][idx2] = table[idx1][column - idx2 - 1]
            table[idx1][column - idx2 - 1] = elem
    return table

line = 3
column = 8
lst = [[0]*column for i in range(line)]
random_table(lst)
print_table(lst)
print()
line_reverse = int(line/2)
column_reverse = int(column/2)
table_revers (lst)
print_table(lst)