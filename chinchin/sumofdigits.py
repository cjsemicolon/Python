number = int(input("Enter a three-digit number: "))

hundreds = number // 100
tens = (number // 10) % 10
ones = number % 10

total = hundreds + tens + ones

print("Sum of digits:", total)
