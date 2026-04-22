"""
psuedocode
Number triangle
Pseudocode
Loop rows 1 to 5
Inner loop from 1 to row number
Print numbers
"""
for row in range(1, 6):
    for column in range(1, row + 1):
        print(column, end=" ")
    print()
