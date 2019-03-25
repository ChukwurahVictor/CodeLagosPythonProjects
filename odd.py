#Print out the purpose of the program
print("This is a program to determine if a number is even")

#Print out the instructions
print("This program will only work for whole numbers")

#Ask the user to enter a number
num = int(input("Please enter a number: "))
odd = num % 2

#Display if the number is odd
if(odd != 0):
    print(num, "is odd")
else:
    print(num, "is not an odd number")
