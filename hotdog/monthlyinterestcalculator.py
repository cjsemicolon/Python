balance = float(input("Enter account balance: "))
annual_interest_rate = float(input("Enter annual interest rate (%): "))

interest = balance * (annual_interest_rate / 1200)

print("Interest for next month:", interest)
