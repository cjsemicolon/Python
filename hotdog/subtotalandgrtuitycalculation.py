subtotal = float(input("Enter the subtotal: "))
gratuity_rate = float(input("Enter the gratuity rate (in %): "))

gratuity = subtotal * (gratuity_rate / 100)
total = subtotal + gratuity

print("Gratuity: $", gratuity)
print("Total: $", total)
