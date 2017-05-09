def create_password ():
    import random
    import string
    lst1 = [c for c in string.ascii_lowercase]
    lst2 = [c for c in string.ascii_uppercase]
    lst3 = [x for x in string.digits]
    full_lst = lst1 + lst2 + lst3 + ['_']
    password=[]
    for i in range (5):
        password.append (full_lst [random.randint(0,len(full_lst)-1)])
    password.append(lst1[random.randint(0,len(lst1))])
    password.append(lst2[random.randint(0,len(lst2))])
    password.append(lst3[random.randint(0,len(lst3))])
    random.shuffle(password)
    password = "".join( [c for c in password])
    return password
print(create_password())