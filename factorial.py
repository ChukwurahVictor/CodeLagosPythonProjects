#Print the purpose of the program
print("This program computes the factorial of a number.")

def main():
    n = eval(input("Enter a non-negative integer: "))
    print("Factorial of", n ,"is", factorial(n))

#Return the factorial for the specified number
def factorial(n):
    if n == 0: #Base case
        return 1
    
    else:
        return n * factorial(n - 1) #Recursive call

main() #Call the main function