"""
collect input
while true collect input
if number int = done
break
"""
largest = None

while True:
    user_input = input("enter number(enter done to stop): ")
    if user_input == "done":
        break
    number = int(user_input)
    if largest is None or number > largest:
        largest = number

    print(largest)  
