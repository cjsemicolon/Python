age = int(input("Enter your age: "))

max_heart_rate = 220 - age

target_min = max_heart_rate * 0.50
target_max = max_heart_rate * 0.85

print("Maximum heart rate:", max_heart_rate)
print("Target heart rate range:", int(target_min), "to", int(target_max))
