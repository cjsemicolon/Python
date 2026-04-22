"""
Loop 1 - 50
if divisible by 3 and 5 print fizzbuzz
else if divisible by 3 print fizz
else if divisible by 5 print buzz
else print number
"""

for number in range (1,51):
    if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("fizz")
elif number % 5 == 0
    print("Buzz")
else:
    print(number)
