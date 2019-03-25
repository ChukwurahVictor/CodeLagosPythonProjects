#Prompt the user for an upper limit
upper_limit = int(input("Enter the upper limit: "))

#Create an empty lists
number_list = []
prime_number_list = []

#Generate values from 2 to the upper limit
for i in range(2, upper_limit, 1):
    number_list.append(i)

print(len(number_list))

#Assign 2 to be the first prime number
prime_number = 2

while(len(number_list) > 0):
    for i in number_list:
        if(i % prime_number == 0):
            #Remove all the multiples of the prime number from the list
            number_list.remove(i)
    print(len(number_list))
    
    #Append the prime numbers to a list of prime numbers
    prime_number_list.append(prime_number)
    prime_number = number_list.pop(0)

#Append the last value in the list
prime_number_list.append(prime_number)

#Print out your list of prime numbers
print(prime_number_list)
       

    