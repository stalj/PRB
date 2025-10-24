#Two variables x and y have values of 7 and 34. Write a program that swaps variable values (x should be 34 and y should be 7). Use an additional, auxiliary variable.

#Hint: It is a good idea to always put a short description of the program in a comment at the beginning of the file. You can use the task text for this.

#Hint: The program file name may contain the section number and task number, e.g. 3-7.py.

###
# A program for swapping two varable values
#
x = 7
y = 34
z = 0 # additional, auxiliary variable
print("Before swapping: x=", x, "y=", y)

# swap the values
z = x
x = y
y = z

print("After swapping: x=", x, "y=", y)