#a - 4 * b / c
print("a - 4 * b / c")
a = int(input("Enter number a"))
b = int(input("Enter number b"))
c=0
while c == 0:
    c = int(input("Enter number c (not equal to 0)"))
result = a - 4 * b/c
print("%d-4*%d/%d = %.4f" %(a,b,c,result) )