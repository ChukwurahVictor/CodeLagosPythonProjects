#Print out the purpose of the program
print("This is a program to test if a year is a leap year")

#Print out the instructions of the program
print("This program takes only years!")

#Prompt the user to enter a year
year = int(input("Please enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("You entered: ", year, "\n and it is a leap year ")
        else:
           print("Not a leap year!")
    else:
        print("You entered: ", year, "\n and it is a leap year")
else:
    print("Not a leap year")
 