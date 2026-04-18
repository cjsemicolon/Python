print("number\tsquare\tcube")

for number in range(6):
    square = number * number
    cube = number * number * number
    
    print(f"{number:>5}{square:>10}{cube:>10}")
