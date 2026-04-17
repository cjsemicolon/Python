"""Create a program that evaluates the strength of a users password based on its length. the program should prompt the user to enter a password, analyze its length, and classify it into 4 categories:very weak, weak strong, or very strong.

less than 8 = very weak
8 = weak
between 8 and 16 = strong
above 16 = very strong

"""

"""psuedocode
collect user input
analyze the length of the characters in the string
use if ststement to determine conditions
"""

password = str(input("Enter password: "))
password_length = len(password)
print(password)

if password_length < 8:
    print("very weak")

if password_length == 8:
    print("weak")

if password_length >= 8 and password_length <=16:
    print("strong")

if password_length > 16:
    print("very strong")
