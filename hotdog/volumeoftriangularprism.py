import math

side = float(input("Enter the length of the triangle side: "))
length = float(input("Enter the length of the prism: "))

area = (math.sqrt(3) / 4) * (side ** 2)
volume = area * length

print("Volume of the triangular prism:", volume)
