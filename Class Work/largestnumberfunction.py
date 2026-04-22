"""
write a function that takes in 3 values and prints the largest
"""

def largest_number(number_one, number_two, number_three):
    largest = number_one
    if number_two > largest:
        largest = number_two
    if number_three > largest:
        largest = number_three
    return largest

print(largest_number(10, 20,30))
    
