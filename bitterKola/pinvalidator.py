pin = int(input("Enter a 4-digit PIN: "))

if 1000 <= pin <= 9999:
    print("Valid PIN")
else:
    print("Invalid PIN")
