# (a * b + 4) / (c - 1)
print("(a * b + 4) / (c - 1)")
a = int(input("Enter number a"))
b = int(input("Enter number b"))
c = int(input("Enter number c"))
if c-1 == 0:
    print("Error, division by 0")
else:
    result = (a * b + 4) / (c - 1)
    print("(%d * %d + 4) / (%d - 1) = %.4f" %(a,b,c,result))