# Для проверки остаточных знаний учеников после летних каникул, учитель младших классов решил начинать каждый урок с того,
# чтобы задавать каждому ученику пример из таблицы умножения, но в классе 15 человек, а примеры среди них не должны повторяться.
# В помощь учителю напишите программу, которая будет выводить на экран 15 случайных примеров из
# таблицы умножения (от 2*2 до 9*9, потому что задания по умножению на 1 и на 10 — слишком просты).
# При этом среди 15 примеров не должно быть повторяющихся (примеры 2*3 и 3*2 и им подобные пары считать повторяющимися)

def print_table(table):
    for line in table:
        for elem in line:
            print(elem, end="\t")
        print()
    return

line = 9
import random
mul_table = [[0]*(line-1) for i in range(line-1)]
for i in range (2,line+1):
    for j in range(2,line+1):
        mul_table [i-2][j-2] = str(i)+'*'+str(j)
print_table(mul_table)
print()

count = 0
lst = []
reverse_lst = []
while count !=15:
    x = random.randint(0,len(mul_table)-1)
    y = random.randint(0,len(mul_table)-1)
    if (x == y) or (mul_table[x][y] in lst) or (mul_table[x][y] in reverse_lst):
        continue
    else:
        count += 1
        print(str(count) + ')', mul_table[x][y])
        lst.append(mul_table[x][y])
        reverse_lst.append(mul_table[x][y][::-1])



