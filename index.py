import random

myChoice = random.randint(1,10)

for i in range (0,6):
    userChoice = int(input("Guess the number: "))
    if userChoice == myChoice:
        print("you guessed it right")
        break
    else:
        if i < 5:
         print("Try Again")
        else:
         print ("Sorry you have exhausted all your chances")
         print ("The number was ", myChoice)

