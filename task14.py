def print_task(n) :
    print ('====================Task'+str(n)+'====================')
    return

#===========================task14===========================
def is_even (number):
    if number % 2 == 0:
        return True

print_task(14)
number = int (input ("Input number: "))
if is_even(number) == True :
    print ("Number is even")
else:
    print ("Number is not even")