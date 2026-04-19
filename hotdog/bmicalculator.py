weight_pounds = float(input("Enter weight in pounds: "))
height_inches = float(input("Enter height in inches: "))

pound_to_kg = 0.45359237
inch_to_meter = 0.0254

weight_kg = weight_pounds * pound_to_kg
height_m = height_inches * inch_to_meter

bmi = weight_kg / (height_m ** 2)

print("Your BMI is:",bmi)
