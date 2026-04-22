"""
psuedocode
collect input
if number > 0 print number
else run a while loop
if number <= 0
collect input again 
"""

number = int(input("Enter a positive integer: "))
if number > 0:
    print(number)
else:
    while number <= 0:
        number = int(input("Enter a positive integer: "))
        
    
