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

def matrix_revers(matrix):
    for idx1 in range(line):
        for idx2 in range(column):
            t_matrix [idx2][idx1] = matrix[idx1][idx2]
    return t_matrix

line = 3
column = 8
matrix = [[0]*column for i in range(line)]
t_matrix = [[0]*line for i in range(column)]
random_table(matrix)
print_table(matrix)
print()
print_table(matrix_revers (matrix))