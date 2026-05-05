
principal = 1000
rate = 1.07

for years in range(10, 31, 10):
    amount = principal * (rate ** years)
    print(f"After {years} years: {amount}")
