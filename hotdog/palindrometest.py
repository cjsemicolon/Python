number = int(input("Enter a three-digit integer: "))

number = abs(number)

hundreds = number // 100
units = number % 10

if hundreds == units:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")
