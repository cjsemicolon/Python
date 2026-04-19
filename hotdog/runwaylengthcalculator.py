takeoff_speed = float(input("Enter take-off speed: "))
acceleration = float(input("Enter acceleration: "))

runway_length = (takeoff_speed ** 2) / (2 * acceleration)

print("Minimum runway length needed:", runway_length, "meters")
