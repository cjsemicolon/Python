exchange_rate = float(input("Enter the exchange rate from dollars to RMB: "))

choice = int(input("Enter 0 to convert dollars to RMB or 1 for RMB to dollars: "))

if choice == 0:
    dollars = float(input("Enter the amount in dollars: "))
    rmb = dollars * exchange_rate
    print("Amount in RMB:", round(rmb, 2))

elif choice == 1:
    rmb = float(input("Enter the amount in RMB: "))
    dollars = rmb / exchange_rate
    print("Amount in dollars:", round(dollars, 2))

else:
    print("Invalid input")
