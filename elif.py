# ask for their numeric grade
grade = int(input("Enter the numeric grade: "))

# if the grade is between 0 and 100
if grade < 0 or grade > 100:
    print("Invalid input. Please enter a grade between 0 and 100.")
else:
    # letter grade based on the grading scale
    if grade >= 90:
        letter_grade = 'A'
    elif grade >= 80:
        letter_grade = 'B'
    elif grade >= 70:
        letter_grade = 'C'
    elif grade >= 60:
        letter_grade = 'D'
    else:
        letter_grade = 'F'

    # letter grade
    print(f"The letter grade is: {letter_grade}")
