"""
Pseudocode
Generate random number
Set attempts = 0
Repeat:
Ask guess
Increase attempts
If guess < number → higher
If guess > number → lower
If equal → correct
Print attempts
"""

import random

target = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Guess: "))
    attempts += 1

    if guess < target:
        print("higher")
    elif guess > target:
        print("lower")
    else:
        print("correct! ({attempts} attempts)")
        break
