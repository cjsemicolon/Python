
edge1 = float(input("Enter first edge: "))
edge2 = float(input("Enter second edge: "))

if edge1 != edge2:
    perimeter = 2 * (edge1 + edge2)
    print("Perimeter of the rectangle:", perimeter)
else:
    print("Invalid input: edges must be different lengths.")
