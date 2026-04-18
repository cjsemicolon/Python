largest = float('-inf')
second_largest = float('-inf')

for count in range(10):
    number = float(input(f"Enter number {count + 1}: "))

    if number > largest:
        second_largest = largest
        largest = number
    elif number > second_largest:
        second_largest = number

print("Largest value:", largest)
print("Second largest value:", second_largest)
