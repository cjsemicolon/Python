side1 = float(input("Enter side 1: "))
side2 = float(input("Enter side 2: "))
side3 = float(input("Enter side 3: "))

# Check if valid triangle
if (side1 + side2 > side3 and
    side1 + side3 > side2 and
    side2 + side3 > side1):

    print("The sides form a valid triangle")

    # Classification
    if side1 == side2 == side3:
        print("Triangle type: Equilateral")
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("Triangle type: Isosceles")
    else:
        print("Triangle type: Scalene")

else:
    print("The sides do NOT form a valid triangle")
