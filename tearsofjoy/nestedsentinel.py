"""
Pseudocode
Repeat:
Ask student name
If empty → stop
Set total, count = 0
Repeat:
Ask score
If -1 → stop
Add to total, increase count
Compute average
Print result
"""
while True:
    name = input("Student: ")
    if name == "":
        break

    total = 0
    count = 0

    while True:
        score = int(input("Score: "))
        if score == -1:
            break
        total += score
        count += 1

    if count > 0:
        avg = total / count
        print(f"{name} avg:", avg)
