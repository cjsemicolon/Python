number = int(input("Enter an integer: "))

both = (number % 4 == 0) and (number % 5 == 0)

either = (number % 4 == 0) or (number % 5 == 0)

exclusive = either and not both

print("Divisible by both 4 and 5:", both)
print("Divisible by 4 or 5:", either)
print("Divisible by 4 or 5 but not both:", exclusive)
