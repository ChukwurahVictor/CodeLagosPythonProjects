import math

#Display the purpose of the program
print("This is a program to solve Quadratic Equations")

#Ask the user to enter the coefficients of a,b,c
a = float(input("Enter the coefficients of a: "))
b = float(input("Enter the coefficients of b: "))
c = float(input("Enter the coefficients of c: "))

#Discrimant
d = (b**2) - (4 * a * c)


if d < 0:
    print("The equation has no real roots!")
    
elif d == 0:
    x = (-b + math.sqrt(d)) / (2 * a)
    print("The root of the equation is", x)
    
else:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print("The roots of the equation are", x1, "and", x2)

