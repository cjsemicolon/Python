minutes = int(input("Enter the number of minutes: "))

minutes_per_hour = 60
hours_per_day = 24
days_per_year = 365

minutes_per_year = minutes_per_hour * hours_per_day * days_per_year

years = minutes // minutes_per_year
remaining_minutes = minutes % minutes_per_year

days = remaining_minutes // (minutes_per_hour * hours_per_day)

print("Years:", years)
print("Days:", days)
