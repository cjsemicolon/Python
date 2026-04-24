total_minutes = int(input("Enter number of minutes: "))

days = total_minutes // (24 * 60)
remaining_minutes = total_minutes % (24 * 60)

hours = remaining_minutes // 60
minutes = remaining_minutes % 60

print("Days:", days)
print("Hours:", hours)
print("Minutes:", minutes)
