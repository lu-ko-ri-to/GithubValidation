# Python program for evaluation one trainee in a bootcamp

trainee_name = input("Enter trainee full name: ")

python_syntax = float(input("Enter trainee score in Python Syntax: "))
problem_solving = float(input("Enter trainee score in Problem Solving: "))
mini_project = float(input("Enter trainee score in Mini Project: "))

# calculate total and average

total_score = python_syntax + problem_solving + mini_project
average_score = total_score / 3

# determine performance grade

if average_score >= 80:
    performance_grade = "Excellent"
elif average_score >= 70:
    performance_grade = "Very Good"
elif average_score >=60:
    performance_grade = "Good"
elif average_score >= 50:
    performance_grade = "Fair"
else:
    grade = "Needs Improvement"

# Determine the completion status

if average_score >= 50:
    completion_status = "Competent"
else:
    completion_status="Not yet Competent"

#Display the report
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

# Save the data into file

file=open("bootcamp_report.txt","a")
file.write(f"Trainee Name: {trainee_name}\n")
file.write(f"Python Syntax Score: {python_syntax}\n")
file.write(f"Problem Solving Score: {problem_solving}\n")
file.write(f"Mini Project Score: {mini_project}\n")
file.write(f"Total Score: {total_score}\n")
file.write(f"Average Score: {average_score}\n")
file.write(f"Performance Grade: {performance_grade}\n")
file.write(f"Completion Status: {completion_status}\n")
file.close()
print("\n Record saved successfully in the Bootcamp_report.csv")