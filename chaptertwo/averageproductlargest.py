first_number = input("Input first number ")
second_number= input("Input second number ")
third_number = input("Input third number ")

first_number = int(first_number)
second_number = int(second_number)
third_number = int(third_number)

sum = first_number + second_number + third_number
print("sum: ", sum)

average = sum//3
print("average: ", average)

product = first_number * second_number * third_number
print("product: ", product)

largest_number = first_number

if second_number > first_number:
    largest_number = second_number

if third_number > second_number:
    largest_number = third_number

print("the largest number is: ", largest_number)
