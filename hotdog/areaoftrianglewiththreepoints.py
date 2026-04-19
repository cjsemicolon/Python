import math

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))

x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

x3 = float(input("Enter x3: "))
y3 = float(input("Enter y3: "))

side1 = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
side2 = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
side3 = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)

semi_perimeter = (side1 + side2 + side3) / 2

area = math.sqrt(semi_perimeter * (semi_perimeter - side1) * (semi_perimeter - side2) * (semi_perimeter - side3))

print("Area of the triangle:",area)
