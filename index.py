import random

myChoice = random.randint(1,10)

for i in range (0,6):
    userChoice = int(input("Guess the number: "))
    if userChoice == myChoice:
        print("you guessed it right")
        break
    else:
        if i < 5:
            if userChoice > myChoice:
                print("The number is smaller than your guess")
            else:
                print("The number is greater than your guess")
        else:
         print ("Sorry you have exhausted all your chances")
         print ("The number was ", myChoice)

