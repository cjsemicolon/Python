num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if num1 > num2:
    larger = num1
    smaller = num2
else:
    larger = num2
    smaller = num1

total = num1 + num2
difference = num1 - num2
product = num1 * num2

print("Larger value:", larger)
print("Smaller value:", smaller)
print("Sum:", total)
print("Difference:", difference)
print("Product:", product)

if num2 == 0:
    print("Quotient: Cannot divide by zero")
else:
    print("Quotient:", num1 / num2)
