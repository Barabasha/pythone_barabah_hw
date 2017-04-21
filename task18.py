def sum_char(char1, char2) :
    sum = 0
    if ord(char2) > ord(char1):
        for char_code in range (ord(char1), ord(char2)+1):
            sum = sum + char_code
        return sum
    else:
        for char_code in range (ord(char2), ord(char1)+1):
            sum = sum + char_code
        return sum

char1 = input ("Введите первый символ")
char2 = input ("Введите второй символ")
print("Сумма кодов символов между", char1, "и", char2, "=", sum_char(char1,char2))



