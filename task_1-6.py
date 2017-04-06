print ("=====================Task1====================")
#a + b * ( c / 2 )
a = 5
b = 7
c = 5
Result = a + b * ( c / 2 )
print ("Result of a+b*(c/2) ( a=%d, b=%d, c=%d ) is %.2f" %(a,b,c,Result))
print ()

print ("=====================Task2====================")
#(a^2 + b^2) % 2
a = 4
b = 7
Result = (a**2 + b**2) % 2
print ("Result of (a^2 + b^2) %% 2 ( a=%d, b=%d ) is %d" %(a,b,Result))
print ()


print ("=====================Task3====================")
#(a - b * c ) / ( a + b ) % c
a = 5
b = 7
c = 3
Result = ( a + b ) / 12 * c % 4 + b
print ("Result of (a+b)/12*c%%4+b ( a=%d, b=%d, c=%d ) is %.2f" %(a,b,c,Result))
print ()

print ("=====================Task4====================")
#(a - b * c ) / ( a + b ) % c
a = 5
b = 7
c = 8
Result = (a - b * c ) / ( a + b ) % c
print ("Result of (a-b*c)/(a+b)%%c ( a=%d, b=%d, c=%d ) is %.4f" %(a,b,c,Result))
print ()

print ("=====================Task5====================")
#| a - b | /( a + b)^3 - cos( c )
import math
a = 2
b = 3
c = 1
Result = math.fabs( a - b ) / ( a + b )**3 - math.cos( c )
print ("Result of |a-b|/(a+b)^3-cos(c) ( a=%d, b=%d, c=%d ) is %.4f" %(a,b,c,Result))
print ()

print ("=====================Task6====================")
#( ln( 1 + c ) / -b )^4 + | a |
import math
a = - 4
b = 0.5
c = math.e - 1
Result = (math.log( 1 + c ) / ( - b ))**4 + math.fabs( a )
print ("Result of (ln(1+c)/-b)^4+|a| ( a=%d, b=%.1f, c=%.8f ) is %.4f" %(a,b,c,Result))

