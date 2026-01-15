###
# A program that calculates the length of the diagonal
# of a rectangle with sides a and b.
#
import math
a = float(input('Enter the length of side a: '))
b = float(input('Enter the length of side b: '))    
diagonal = math.sqrt(a**2 + b**2)
print('Diagonal: ', diagonal)