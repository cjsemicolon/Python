student_score = input("Enter score: ")

student_score = int(student_score)

if student_score >= 90 and student_score  <= 100:
    print("A")
elif student_score >= 80 and student_score  <= 89:
    print("B")
elif student_score >= 70 and student_score  <= 79:
    print("C")
elif student_score >= 60 and student_score  <= 69:
    print("D")
else:
    print("F")
