def print_task(n) :
    print ('====================Task'+str(n)+'====================')
    return

#===========================task16===========================
def accident(v1,v2):
    if v2 == 0:  #если 2 поезд стоит - аварии не будет
        return False
    elif v1== 0:
        return True #если 1 поезд стоит - авария
    elif 6/v2 <= 4/v1 :
        return True  #если до запасного пути раньше (или в тоже время)доедет 2 поезд - авария
    else:
        return False

print_task(16)
v1 = int(input ("Input speed of train№1"))
v2 = int(input ("Input speed of train№2"))

if accident(v1,v2)==True:
    print ("Accident")
else:
    print ("Good")