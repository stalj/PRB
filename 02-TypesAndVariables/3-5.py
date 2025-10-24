#Write a program that calculates the length of the diagonal of a rectangle with sides a=5 and b=8. 
#To calculate the square root of a given value, use the sqrt function. The function is available in a module called math, which you must import into your program.

###
# A program that calculates the length of the diagonal
# of a rectangle with sides a and b.
#
import math
a = 5
b = 8
diagonal = math.sqrt(a**2+b**2)
print(diagonal)