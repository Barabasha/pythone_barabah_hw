print ("Простые числа:")
print(2)
for x in range (3,101):
    count = 0
    for y in range (2,x):
        count = 0
        if x%y == 0 :
            break
        else: count=1
    if count == 1:
        print (x)
