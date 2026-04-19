seconds_per_year = 365 * 24 * 60 * 60

current_population = 312032486

birth_rate_per_second = 7
death_rate_per_second = 13
immigration_rate_per_second = 45

births_per_year = seconds_per_year // birth_rate_per_second
deaths_per_year = seconds_per_year // death_rate_per_second
immigrants_per_year = seconds_per_year // immigration_rate_per_second

yearly_population_change = births_per_year - deaths_per_year + immigrants_per_year

years = int(input("Enter number of years: "))

population = current_population

for _ in range(years):
    population += yearly_population_change

print("Population after", years, "years:", population)
