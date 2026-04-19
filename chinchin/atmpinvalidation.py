pin = int(input("Enter your PIN: "))

correct_pin = 1234
balance = 1000

if pin == correct_pin:
    print("PIN correct")
    print("Your balance is $", balance)
else:
    print("Incorrect PIN")
