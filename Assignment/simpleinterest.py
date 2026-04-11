principal = input("Input principal: ")
rate = input("Input rate in %: ")
time = input("Input time in years: ")

principal = int(principal)
rate = int(rate )
time = int(time)

simple_interest = (principal * rate * time)/100

print(simple_interest)

total_amount = principal + simple_interest
print(total_amount)
