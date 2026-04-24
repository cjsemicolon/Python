speed = float(input("Enter speed in km/h: "))

if speed == 0:
    print("Stationary")
elif 1 <= speed <= 40:
    print("Slow")
elif 41 <= speed <= 80:
    print("Moderate")
elif 81 <= speed <= 120:
    print("Fast")
else:
    print("Dangerously Fast")
