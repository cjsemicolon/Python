wage = float(input("Enter hourly wage: "))
hours = float(input("Enter hours worked: "))

if hours <= 40:
    total_pay = wage * hours
else:
    overtime_hours = hours - 40
    total_pay = (40 * wage) + (overtime_hours * wage * 1.5)

print("Total earnings:", total_pay)
