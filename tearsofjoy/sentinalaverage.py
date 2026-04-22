"""
Pseudocode
Set sum = 0, count = 0
Repeat:
Ask number
If -1 → stop
Add to sum
Increase count
Compute average
"""

total = 0
count = 0

while True:
    number = int(input("Enter: "))
    if number == -1:
        break
    total += number
    count += 1

if count > 0:
    print("Count:", count, "Average:", total / count)
