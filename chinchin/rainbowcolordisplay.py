import random

number = random.randint(1, 7)

if number == 1:
    color = "Violet"
elif number == 2:
    color = "Indigo"
elif number == 3:
    color = "Blue"
elif number == 4:
    color = "Green"
elif number == 5:
    color = "Yellow"
elif number == 6:
    color = "Orange"
else:
    color = "Red"

print("Random number:", number)
print("Rainbow color:", color)
