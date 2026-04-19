water_mass_kg = float(input("Enter amount of water in kilograms: "))
initial_temperature_c = float(input("Enter initial temperature: "))
final_temperature_c = float(input("Enter final temperature: "))

temperature_change = final_temperature_c - initial_temperature_c

energy_needed_joules = water_mass_kg * temperature_change * 4184

print("Energy needed to heat the water (in joules):", energy_needed_joules)
