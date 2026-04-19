number = int(input("Enter a 4-digit integer: "))

thousands = number // 1000
hundreds = (number // 100) % 10
tens = (number // 10) % 10
ones = number % 10

reversed_number = (ones * 1000) + (tens * 100) + (hundreds * 10) + thousands

print("Reversed number:", reversed_number)
