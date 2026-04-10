'''(Fill in the missing code) Replace *** in the following code with a statement that
will print a message like 'Congratulations! Your grade of 91 earns you an A in this
course'. Your statement should print the value stored in the variable grade:'''

grade = input("Input your grade: ")
grade = int(grade)
print(type(grade))
if grade >= 90:
    print("Congratulations your grade of ", "grade earns you an A in thia course.")
