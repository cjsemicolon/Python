radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

pi = 3.142

radius_square = radius * radius

surface_area = (2 * pi * radius_square) + (2 * pi * radius * height)
volume = pi * radius_square * height

print("Surface Area:", surface_area)
print("Volume:", volume)
