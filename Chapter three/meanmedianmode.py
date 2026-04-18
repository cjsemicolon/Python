numbers = [9, 11, 22, 34, 17, 22, 34, 22, 40]

mean = sum(numbers) / len(numbers)

numbers.sort()
number_length = len(numbers)
median = numbers[number_length // 2]


print("Mean:", mean)
print("Median:", median)


"""
if we add another 34 then there will be 2 modes because 34 will now appear 3 times like 22
"""
