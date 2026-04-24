price = float(input("Enter the original price: "))
discount_percent = float(input("Enter discount percentage: "))

discount_amount = (discount_percent / 100) * price

final_price = price - discount_amount

print("Discount amount:", discount_amount)
print("Final price:", final_price)
