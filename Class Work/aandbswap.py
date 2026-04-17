'''A student wants to swap a = 5 and b =10 so that a becomes 10 and b becomes 5.they write a = b and b = a explain the bug . write the correct solution.'''

first_number = 5
second_number = 10

'''third_number = first_number
first_number = second_number

second_number = third_number

print(first_number,+ second_number) 

#the bug in the original code is that once you make b = a you lose a so you need to store a somewhere else first

this is another way of doing it below
'''
first_number,second_number = second_number, first_number

print(first_number,+ second_number) 
