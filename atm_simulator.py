#Display the purpose of the program
print("This is program to display the operations of an ATM")

#Display the instructions
print("Please select the letter with the option you want to perform.")

#Assigning some pin
victorPin = 1234
paulPin = 2345
charlesPin = 3456

#Ask the user to enter his/her pin
pin = int(input("Please Enter your Pin: "))

#Check Pin
if pin == victorPin:
    print("\nWelcome Mr Victor!\n")

elif pin == paulPin:
    print("\nWelcome Mr Paul!\n")

elif pin == charlesPin:
    print("\nWelcome Mr Charles!\n")

else:
    print("Invalid Pin!\n")

#Menu
menu = input("What would you like to do?\n(a) Withdrawal\n(b) Balance Enquiry\n(c) Transfer\n(d) Change pin\n>>> ")

#For Withdrawal
if menu.lower() == "a":
    amount = input("\nHow much would you like to withdraw:\n(a) #1,000\n(b) #5,000\n(c) #10,000\n(d) #15,000\n(e) #20,000\n(f) Others\n>>> ")

    if amount.lower() == "f":
        other_amount = int(input("\nPlease enter amount: #"))

        trial = other_amount < 1000 or other_amount > 20000 or other_amount % 1000 != 0
        
        while trial is True:
            other_amount = int(input("\nInvalid amount!\nPlease re-enter amount: #"))

        else:
            account_type = input("\nSelect your account type:\n(a) Current\n(b) Savings\n>>> ")

        if account_type.lower() == "a":
            receipt = input("\nDo you want a receipt:\n(a) Yes\n(b) No\n>>> ")

            if receipt == "a":
                print("Transaction in Progress...")

            elif receipt == "b":
                print("Transaction in Progress...")

            else:
                receipt = input("Invalid input!\nDo you want a receipt:\n(a) Yes\n(b) No\n>>> ")

        elif account_type == "b":
            receipt = input("Do you want a receipt:\n(a) Yes\n(b) No\n>>> ")

            if receipt == "a":
                print("Transaction in Progress...")

            elif receipt == "b":
                print("Transaction in Progress...")

            else:
                receipt = input("Invalid input!\nDo you want a receipt:\n(a) Yes\n(b) No\n>>> ")
                
        else:
            account_type = input("Invalid input!\nSelect your account type:\n(a) Current\n(b) Savings\n>>> ")

    elif amount.lower() == "a" or "b" or "c" or "d" or "e":
        account_type = input("\nSelect your account type:\n(a) Current\n(b) Savings\n>>> ")

        if account_type.lower() == "a":
            receipt = input("\nDo you want a receipt:\n(a) Yes\n(b) No\n>>> ")

            if receipt == "a":
                print("Transaction in Progress...")

            elif receipt == "b":
                print("Transaction in Progress...")

            else:
                receipt = input("Invalid input!\nDo you want a receipt:\n(a) Yes\n(b) No\n>>> ")

        elif account_type == "b":
            receipt = input("Do you want a receipt:\n(a) Yes\n(b) No\n>>> ")

            if receipt == "a":
                print("Transaction in Progress...")

            elif receipt == "b":
                print("Transaction in Progress...")

            else:
                receipt = input("Invalid input!\nDo you want a receipt:\n(a) Yes\n(b) No\n>>> ")
                
        else:
            account_type = input("Invalid input!\nSelect your account type:\n(a) Current\n(b) Savings\n>>> ")



#For Balance Enquiry
if menu.lower() == "b":
    account_type = input("Select your account type:\n(a) Current\n(b) Savings\n>>>")

    if account_type.lower() == "a" or account_type == "b":
        receipt = input("Do you want receipt:\n(a) Yes\n(b) No\n>>>")

        if receipt.lower() == "a" or receipt.lower() == "b":
            print("Transaction in progress...")

        else:
            print("Invalid input!")

    else:
        print("Invalid input!")
'''
#For Transfer
if menu.lower() == "c":
    mode_of_transfer = input("How do you want to transfer:\n(a) Quickteller\n(b) ")

    if mode_of_transfer == "a":
        select_bank = input("Please select the bank:\n(a) Access Bank\n(b) Fidelity Bank\n(c) GT Bank\n(d) UBA Bank\n(e) Zenith Bank")

        if select_bank.lower() == "a" or select_bank.lower() == "b" or select_bank.lower() == "c" or select_bank.lower() == "d" or select_bank.lower() == "e":
            
'''