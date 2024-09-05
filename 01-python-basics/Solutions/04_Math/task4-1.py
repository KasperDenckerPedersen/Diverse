'''
Create a program that allows the user to enter 2 numbers representing the width and length of a rectangle. 
The program calculates and displays the area of the rectangle.
'''

width = float(input("Width of the rectangle: "))
length = float(input("Length of the rectangle: "))

area = width * length

print(f'The area of the rectangle with width {width} and length {length} is {area}')