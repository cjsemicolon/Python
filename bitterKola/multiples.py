number1 = int(input("Enter the first integer: "))
number2 = int(input("Enter the second integer: "))

if number2 == 0:
    print("Cannot determine (division by zero).")
else:
    if number1 % number2 == 0:
        print(number1, "is a multiple of", number2)
    else:
        print(number1, "is NOT a multiple of", number2)
