# Python program for evaluation of one trainee in a bootcamp
# This program includes input validation, grading, report display, and file saving

# -------------------------------------------------
# FUNCTION FOR VALIDATING SCORE INPUT
# -------------------------------------------------
def get_valid_score(subject):
    # This function ensures the user enters a number between 0 and 100
    while True:
        try:
            score = float(input(f"Enter trainee score in {subject}: "))
            if 0 <= score <= 100:
                return score
            else:
                print("Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# -------------------------------------------------
# INPUT SECTION WITH VALIDATION
# -------------------------------------------------

# Validate trainee name (should not be empty)
while True:
    trainee_name = input("Enter trainee full name: ").strip()
    if trainee_name == "":
        print("Name cannot be empty. Please enter again.")
    else:
        break

# Get validated scores
python_syntax = get_valid_score("Python Syntax")
problem_solving = get_valid_score("Problem Solving")
mini_project = get_valid_score("Mini Project")

# -------------------------------------------------
# PROCESSING SECTION (CALCULATIONS)
# -------------------------------------------------

# Calculate total and average score
total_score = python_syntax + problem_solving + mini_project
average_score = total_score / 3

# -------------------------------------------------
# DECISION SECTION (GRADE & COMPLETION STATUS)
# -------------------------------------------------

# Determine performance grade
if average_score >= 80:
    performance_grade = "Excellent"
elif average_score >= 70:
    performance_grade = "Very Good"
elif average_score >= 60:
    performance_grade = "Good"
elif average_score >= 50:
    performance_grade = "Fair"
else:
    performance_grade = "Needs Improvement"

# Determine completion status
if average_score >= 50:
    completion_status = "Competent"
else:
    completion_status = "Not yet Competent"

# -------------------------------------------------
# OUTPUT SECTION (DISPLAY REPORT)
# -------------------------------------------------

print("\n========================================")
print("Python Bootcamp Trainee Report")
print("========================================\n")
print("Trainee Name:", trainee_name)
print("Python Syntax Score:", python_syntax)
print("Problem Solving Score:", problem_solving)
print("Mini Project Score:", mini_project)
print("Total Score:", total_score)
print("Average Score:", average_score)
print("Performance Grade:", performance_grade)
print("Completion Status:", completion_status)
print("==============================================")

# -------------------------------------------------
# FILE SAVING SECTION
# -------------------------------------------------

# Open file in append mode so new records are added
file = open("bootcamp_report.txt", "a")

# Write trainee report into file
file.write(f"Trainee Name: {trainee_name}\n")
file.write(f"Python Syntax Score: {python_syntax}\n")
file.write(f"Problem Solving Score: {problem_solving}\n")
file.write(f"Mini Project Score: {mini_project}\n")
file.write(f"Total Score: {total_score}\n")
file.write(f"Average Score: {average_score}\n")
file.write(f"Performance Grade: {performance_grade}\n")
file.write(f"Completion Status: {completion_status}\n")
file.write("====================================\n")

# Close the file
file.close()

print("\nRecord saved successfully in bootcamp_report.txt")