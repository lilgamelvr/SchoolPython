import random

compNum = random.randint(1, 50)
guess = input("Guess a number between 1 and 50")
guess = int(guess)

if guess > compNum:
    print("too high")
    print(compNum)
elif guess < compNum:
    print("too low")
    print(compNum)
else:
    print("correct")
    print(compNum)
