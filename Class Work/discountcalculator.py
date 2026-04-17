"""Design a program that applies tiered discounts based on a customers total spending in a store. The greater the purchase amount the higher the discount offered.
purchases between 1000 and 10000 receive a 5% discount
purchases between 10000 and 50000 receive 10% discount
purchase above 50000 receive 20% discount

ensure the program calculates and displays the appropirate discount for the given amount

"""

"""
Psuedo code
collect purchase amount
define rule for calculating percentage discount
if purchase amount is 1000 to 10000 apply 5% discount
print results
"""

purchase_amount = int(input("Enter amount purchased: "))

five_percent_discount = 0.05 * purchase_amount
ten_percent_discount = 0.10 * purchase_amount
twenty_percent_discount = 0.20 * purchase_amount

if purchase_amount > 1000 and purchase_amount <= 10000:
    purchase_amount = purchase_amount - five_percent_discount

    print(purchase_amount)

if purchase_amount > 10000 and purchase_amount <= 50000:
    purchase_amount = purchase_amount - ten_percent_discount

    print(purchase_amount)

if purchase_amount > 50000: 
    purchase_amount = purchase_amount - twenty_percent_discount

    print(purchase_amount)
