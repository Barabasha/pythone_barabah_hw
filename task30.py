def string2list (str): #Перевод строки в список
    lst = []
    for i in range(len(str)):
        lst.append(str[i])
    return lst

key = 5
cipher_str = '1qaz2\"\'wsx3edc4rfv5tgb6yhn7ujm8ik,9ol.0p;/-[=]\!йфяцыч№увс;кам%епи:нрт?гоьшлб*(щдю )зж._хэ+ъQAZWSXEDCRFVTGBYHNUJMIKOLPЙФЯЦЫЧУВСКАМЕПИНРТГОЬШЛБЩДЮЗЖХЭЪЁ'
user_str = input("Enter text")
user_lst = string2list(user_str)
for i in range(len(user_lst)): #шифрование
    idx_char = cipher_str.find(user_str[i])
    if idx_char + key >= len(cipher_str): #выход за границу списка с положительным ключом
        user_lst[i] = cipher_str[idx_char - len(cipher_str) + key]
    elif idx_char + key < 0: #выход за границу списка с отрицательным ключом
        user_lst[i] = cipher_str [len(cipher_str) + idx_char + key ]
    else:
        user_lst[i] = cipher_str[idx_char + key]
new_user_str = ''
for i in range(len(user_lst)):#Перевожу зашифрованный список в строку для читабельности
    new_user_str += user_lst[i]
print(new_user_str)



