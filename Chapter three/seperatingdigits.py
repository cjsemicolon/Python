number = 54321

individual_digits = []

while number > 0:
    digits.append(number % 10)
    number = number//10
digits.reverse()
print(digits)    
    
