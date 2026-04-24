day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

valid = True

if month < 1 or month > 12:
    valid = False
else:
    days_in_month = [31, 28, 31, 30, 31, 30,
                      31, 31, 30, 31, 30, 31]

    leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    if leap_year:
        days_in_month[1] = 29

    if day < 1 or day > days_in_month[month - 1]:
        valid = False

if valid:
    print("Valid date")
else:
    print("Invalid date")
