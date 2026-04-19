monthly_saving = float(input("Enter monthly saving amount: "))

monthly_interest_rate = 0.003125

# Month 1
month1 = monthly_saving * (1 + monthly_interest_rate)

# Month 2
month2 = (monthly_saving + month1) * (1 + monthly_interest_rate)

# Month 3
month3 = (monthly_saving + month2) * (1 + monthly_interest_rate)

# Month 4
month4 = (monthly_saving + month3) * (1 + monthly_interest_rate)

# Month 5
month5 = (monthly_saving + month4) * (1 + monthly_interest_rate)

# Month 6
month6 = (monthly_saving + month5) * (1 + monthly_interest_rate)

print("After month 1:", month1
print("After month 2:", month2
print("After month 3:", month3
print("After month 4:", month4
print("After month 5:", month5
print("After month 6:", month6
