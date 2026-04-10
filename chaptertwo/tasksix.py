'''(Odd or Even) Use if statements to determine whether an integer is odd or even.'''

integer = input("Input integer: ")
integer = int(integer)
if integer % 2 == 0:
    print("Even number")
else:
    print("Odd number")
