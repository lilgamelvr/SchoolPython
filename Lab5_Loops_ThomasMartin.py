import random

numGuess = 0
maxGuess = 7
compNum = random.randint(1,50)

while numGuess < maxGuess:
    guess = input("Guess a number between 1 and 50")
    guess = int(guess)
    if guess == compNum:
        print("You Win")
        break
    numGuess += 1
else:
    print("Game over")