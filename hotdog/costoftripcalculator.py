distance_miles = float(input("Enter distance to drive (miles): "))
fuel_efficiency_mpg = float(input("Enter fuel efficiency (miles per gallon): "))
price_per_gallon = float(input("Enter price per gallon: "))

gallons_needed = distance_miles / fuel_efficiency_mpg
trip_cost = gallons_needed * price_per_gallon

print("Cost of the trip:",trip_cost)
