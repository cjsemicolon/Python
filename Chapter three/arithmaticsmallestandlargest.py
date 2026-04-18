numbers = []

for digit in range(3):
    figure = int(input(f"Enter a figure{digit + 1}: "))
    numbers.append(figure)

total = sum(numbers)
print("sum: ", total)

average = total//3
print("average: ", average)

product = numbers[0] * numbers[1] * numbers[2]
print("product: ", product)

largest_number = numbers[0]

if numbers[1] > numbers[0]:
    largest_number =  numbers[1]

if numbers[2] > numbers[1]:
    largest_number = numbers[2]

print("the largest number is: ", largest_number)
