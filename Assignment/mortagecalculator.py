# Mortgage Calculator

principal = float(input("Input Principal: "))
annual_rate = float(input("Input rate in %: "))
years = int(input("Input time in years: "))

monthly_rate = annual_rate / 100 / 12   
months = years * 12                     

monthly_payment = principal * (monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)

print("Your monthly mortgage payment is: ", + monthly_payment)
