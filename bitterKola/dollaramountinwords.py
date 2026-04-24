words = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten"
}

amount = int(input("Enter a dollar amount (1 to 10): "))

if 1 <= amount <= 10:
    print(words[amount], "dollars")
else:
    print("Invalid input. Enter a number from 1 to 10.")
