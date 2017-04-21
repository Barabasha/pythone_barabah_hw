print("Числа от 0 до 1000, которые содержат в себе цифры 1 и 7 :")
for x in range(0,1001):
    string = str(x)
    if string.find('7') != -1 and string.find('1') != -1:
        print(x)

