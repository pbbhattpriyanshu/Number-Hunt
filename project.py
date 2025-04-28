import random

print("Guess the number between 1 to 100")
target = random.randint(1, 100)

while True:
    userChoice = (input("Guess the target or Quit(Q): "))
    if (userChoice == "Q"):
        break

    userChoice = int(userChoice)
    if (userChoice == target):
        print("Success :  Correct guess!!")
        break
    elif (userChoice < target):
        print("Your Number is too small. Take a bigger guess..")
    else:
        print("Your Number is too big. Take a smaller guess..")

print("Game is over..............")