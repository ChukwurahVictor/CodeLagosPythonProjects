#Print the purpose of the program
print("This program computes the fibonacci series of a number")

def main():
    index = eval(input("Enter the index: "))
    print("The Fibonacci number at", index, "is", fibonacci(index))
    
    
def fibonacci(index):
    if index == 0:
        return 0

    elif index == 1:
        return 1
        
    else:
        return (fibonacci(index - 1) + fibonacci(index - 2))

main()