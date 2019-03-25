 #prints the purpose of the program
print("This is a Multiplication times table")

for i in range(1, 21):
    print(i, "times table")

    for j in range(1,13):
        print(i, "*", j ,"=", i * j)

    print("\n")
