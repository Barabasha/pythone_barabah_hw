def create_password ():
    import random
    lst1 = [c for c in 'qwertyuiopasdfghjklzxcvbnm']
    lst2 = [c for c in 'QWERTYUIOPASDFGHJKLZXCVBNM']
    lst3 = [str(x) for x in range(0,10)]
    full_lst = lst1 + lst2 + lst3 + ['_']
    password=[]
    for i in range (5):
        password.append (full_lst [random.randint(0,len(full_lst)-1)])
    password.append(lst1[random.randint(0,25)])
    password.append(lst2[random.randint(0,25)])
    password.append(lst3[random.randint(0,9)])
    random.shuffle(password)
    password = "".join( [c for c in password])
    return password
print(create_password())