score = 140

if score>101:
    print("Invalid grade")
    exit()

if  score >= 90:
    grade = "A"
elif score>= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score>=60:
    grade = "D"
else:
    grade = "F"

print("Grade:",grade)