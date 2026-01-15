###
# A program that calculates and prints
# the average grade of a student
#
math = float(input('Enter grade for Math: '))
art = float(input('Enter grade for Art: '))
music = float(input('Enter grade for Music: '))
history = float(input('Enter grade for History: ')) 

average = (math + art + music + history) / 4
print("Average grade is", average)