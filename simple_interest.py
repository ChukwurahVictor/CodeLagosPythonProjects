#Display the purpose of the program
print("This program calculates simple interest")

#Prompt the user to enter the principal amount
principal = float(input("Enter the principal amount: "))

#Prompt the user to enter the rate
rate = float(input("Enter the rate: "))

#Prompt the user to enter the time period
time = float(input("Enter the time period: "))

#Calculate the Simple interest
simple_interest = (principal * rate * time) / 100 

#Print the Simple interest
print(round(simple_interest, 2))