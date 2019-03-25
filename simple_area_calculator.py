import math

#Display the purpose of the program
print("This is a program to calculate the area of different shapes")

#Display the instructions
print("Select the letter of the option with the shape you want to calculate")

#Ask the user to enter the shape you want to calculate for
shape = input("Please, enter a shape: \n(a) Circle\n(b) Square\n(c) Triangle\n(d) Rectangle\nInput: ")

#For Circle
if shape.lower() == "a":
    radius = float(input("Enter the radius of the Circle: "))
    area = math.pi * (radius * radius)

    print("The area of the Circle is: ", area)

#For Square
if shape.lower() == "b":
    length = float(input("Enter the length of the Square: "))
    area = length * length

    print("The area of the Square is: ", area)

#For Triangle
if shape.lower() == "c":
    base = float(input("Enter the base of the Triangle: "))
    height = float(input("Enter the height of the Triangle: "))
    area = (1 / 2) * base * height

    print("The area of the Triangle is: ", area)

#For Rectangle
if shape.lower() == "d":
    base = float(input("Enter the base of the Rectangle: "))
    height = float(input("Enter the height of the Rectangle: "))
    area = base * height

    print("The area of the Rectangle is: ", area)
