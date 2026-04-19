import random

coin = random.randint(0, 1)

guess = int(input("Enter your guess (0 for Heads, 1 for Tails): "))

if guess == coin:
    print("Correct!")
else:
    print("Wrong!")

if coin == 0:
    print("The coin was Heads")
else:
    print("The coin was Tails")
