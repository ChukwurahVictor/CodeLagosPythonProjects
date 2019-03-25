# Display the purpose of the program
print("This is a Quiz")

#Display the instructions
print("Select the letter with the correct option")
print("This program uses the negative marking system")

#Initialize score
score = 0

#Ask the user the first question
question1 = input("1. Who won the 2018 Balon d'or award?\n(a) Luka Modric\n(b) Cristiano Ronaldo\n(c) Lionel Messi\n(d) Antoine Griezman\nYour answer: ")

#Check if the question is right
if question1.lower() == "a":
    print("Correct")
    score = score + 1  #Increment the score

else:
    print("Wrong \nThe Correct answer is 'a'")
    score = score - 1 #Increment the score

#Ask the user the second question
question2 = input("2. How many times has Cristiano Ronaldo won the Balon d'or award?\n(a) 3\n(b) 5\n(c) 4\n(d) 6\nYour answer: ")

#Check if the question is right
if question2.lower() == "b":
    print("Correct")
    score = score + 1  #Increment the score

else:
    print("Wrong \nThe Correct answer is 'b'")
    score = score - 1  #Decrement the score

#Ask the user the third question
question3 = input("3. Which of the following players has NOT won the Balon d'or award?\n(a) Kaka\n(b) Modric\n(c) Iniesta\n(d) Ronaldo\nYour answer: ")

#Check if the answer is right
if question3.lower() == "c":
    print("Correct")
    score = score + 1   #Increment the score

else:
    print("Wrong \nThe Correct answer is 'c'")
    score = score - 1 #Decrement the score

#Ask the user the fouth question
question4 = input("4. The Balon d'or award started in the year ______?\n(a) 1957\n(b) 1959\n(c) 1956\n(d) 1958\nYour answer: ")

#Check if the answer is right
if question4.lower() == "c":
    print("Correct")
    score = score + 1  #Increment the score

else:
    print("Wrong \nThe Correct answer is 'c'")
    score = score - 1 #Decrement the score

#Ask the next question
question5  = input("5. Who was the first receipient of the Balon d'or award?\n(a) Alfredo Di Stefano\n(b) Franz Beckenbauer\n(c) Johann Cryuff\n(d) Stanley Matthews\nYour answer: ")

#Check if the answer is right
if question5.lower() == "d":
    print("Correct")
    score = score + 1 #Increment the score

else:
    print("Wrong \nThe Correct answer is 'd'")
    score = score - 1 #Decrement the score


if score < 0:
    print("Your total score is 0")

else:
    print("Your total score is", score)
