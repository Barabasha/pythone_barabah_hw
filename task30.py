def string2list (str): #Перевод строки в список
    lst = []
    for i in range(len(str)):
        lst.append(str[i])
    return lst

cipher_str = '1qaz2\"\'wsx3edc4rfv5tgb6yhn7ujm8ik,9ol.0p;/-[=]\!йфяцыч№увс;кам%епи:нрт?гоьшлб*(щдю )зж._хэ+ъQAZWSXEDCRFVTGBYHNUJMIKOLPЙФЯЦЫЧУВСКАМЕПИНРТГОЬШЛБЩДЮЗЖХЭЪЁ1qaz2'
user_str = input("Enter text")
user_lst = string2list(user_str)
for i in range(len(user_lst)): #шифрование
    user_lst[i] = cipher_str[cipher_str.find(user_str[i])+5]
new_user_str = ''
for i in range(len(user_lst)):#Перевожу зашифрованный список в строку для читабельности
    new_user_str += user_lst[i]
print(new_user_str)



