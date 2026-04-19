number = int(input("Enter a 3-digit integer: "))

hundreds = number // 100
tens = (number // 10) % 10
ones = number % 10

if hundreds == ones:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
