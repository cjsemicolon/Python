principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest (%): "))
time = float(input("Enter time (in years): "))

simple_interest = (principal * rate * time) / 100

amount = principal * (1 + rate / 100) ** time
compound_interest = amount - principal

print("Simple Interest:", simple_interest)
print("Compound Interest:", compound_interest)
