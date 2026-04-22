"""
Pseudocode
Set correct password
Allow 3 attempts
If correct → success
Else after 3 → locked
"""
correct = "python123"

for count in range(3):
    password = input("Password: ")
    if password == correct:
        print("Access granted")
        break
else:
    print("Locked out")
