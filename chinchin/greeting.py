hour = int(input("Enter the current hour (0–23): "))

if 5 <= hour <= 11:
    print("Good Morning")
elif 12 <= hour <= 17:
    print("Good Afternoon")
elif 18 <= hour <= 21:
    print("Good Evening")
elif (22 <= hour <= 23) or (0 <= hour <= 4):
    print("Good Night")
else:
    print("Invalid hour")
