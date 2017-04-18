def print_task(n) :
    print ('====================Task'+str(n)+'====================')
    return

#===========================task14===========================
def even (number):
    return number % 2

print_task(14)
number = int (input ("Input number: "))
if even(number) == False :
    print ("Number is even")
else:
    print ("Number is not even")