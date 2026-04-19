velocity = float(input("Enter initial velocity (u) in m/s: "))
time = float(input("Enter time (t) in seconds: "))
acceleration = float(input("Enter acceleration (a) in m/s^2: "))

distance = (velocity * time) + (0.5 * acceleration * time * time)

print("Distance covered: ", distance)
