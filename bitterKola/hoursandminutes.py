hours1 = int(input("Enter first time hours: "))
minutes1 = int(input("Enter first time minutes: "))

hours2 = int(input("Enter second time hours: "))
minutes2 = int(input("Enter second time minutes: "))

total_minutes = minutes1 + minutes2

extra_hours = total_minutes // 60
remaining_minutes = total_minutes % 60

total_hours = hours1 + hours2 + extra_hours

print("Total time:", total_hours, ":", remaining_minutes)
