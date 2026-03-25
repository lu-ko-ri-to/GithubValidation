# ==============================
# SAMSS - Full System with File Handling
# ==============================

import json

# Main data storage
students = {}


# ==============================
# FILE HANDLING FUNCTIONS
# ==============================

def load_from_file():
    global students
    try:
        with open("students.json", "r") as file:
            students = json.load(file)
    except FileNotFoundError:
        students = {}


def save_to_file():
    with open("students.json", "w") as file:
        json.dump(students, file)


# ==============================
# CORE FUNCTIONS
# ==============================

def register_student():
    student_id = input("Enter Student ID: ")

    if student_id in students:
        print("Error: Student ID already exists.")
        return

    name = input("Enter Student Name: ")
    course = input("Enter Course: ")

    students[student_id] = {
        "name": name,
        "course": course,
        "grades": [],
        "attendance": 0,
        "fee_balance": 0
    }

    save_to_file()
    print("Student registered successfully.")


def record_academic_data():
    student_id = input("Enter Student ID: ")

    if student_id not in students:
        print("Student not found.")
        return

    try:
        grade = float(input("Enter Grade (0-100): "))
        attendance = float(input("Enter Attendance (%): "))

        if grade < 0 or grade > 100:
            print("Invalid grade.")
            return

        if attendance < 0 or attendance > 100:
            print("Invalid attendance.")
            return

        students[student_id]["grades"].append(grade)
        students[student_id]["attendance"] = attendance

        save_to_file()
        print("Academic data recorded.")

    except ValueError:
        print("Invalid input.")


def update_fees():
    student_id = input("Enter Student ID: ")

    if student_id not in students:
        print("Student not found.")
        return

    try:
        fee = float(input("Enter Fee Balance: "))

        if fee < 0:
            print("Fee cannot be negative.")
            return

        students[student_id]["fee_balance"] = fee

        save_to_file()
        print("Fee updated successfully.")

    except ValueError:
        print("Invalid input.")


def calculate_average(grades):
    if len(grades) == 0:
        return 0
    return sum(grades) / len(grades)


def check_warning(student):
    avg = calculate_average(student["grades"])
    warnings = []

    if avg < 50:
        warnings.append("Low academic performance")

    if student["attendance"] < 75:
        warnings.append("Low attendance")

    if student["fee_balance"] > 0:
        warnings.append("Fee balance pending")

    return warnings


def display_student():
    student_id = input("Enter Student ID: ")

    if student_id not in students:
        print("Student not found.")
        return

    student = students[student_id]
    avg = calculate_average(student["grades"])
    warnings = check_warning(student)

    if warnings:
        status = "ACADEMIC WARNING"
    else:
        status = "GOOD STANDING"

    # ===== DISPLAY =====
    print("\n===== STUDENT REPORT =====")
    print("ID:", student_id)
    print("Name:", student["name"])
    print("Course:", student["course"])
    print("Average Grade:", round(avg, 2))
    print("Attendance:", student["attendance"], "%")
    print("Fee Balance:", student["fee_balance"], "KES")
    print("Status:", status)

    if warnings:
        for w in warnings:
            print("Warning:", w)

    # ===== SAVE REPORT TO TEXT FILE =====
    with open("student_report.txt", "a") as file:
        file.write(f"Student ID: {student_id}\n")
        file.write(f"Name: {student['name']}\n")
        file.write(f"Course: {student['course']}\n")
        file.write(f"Average Grade: {round(avg, 2)}\n")
        file.write(f"Attendance: {student['attendance']}%\n")
        file.write(f"Fee Balance: {student['fee_balance']} KES\n")
        file.write(f"Status: {status}\n")

        if warnings:
            for w in warnings:
                file.write(f"Warning: {w}\n")

        file.write("====================================\n")

    print("Report saved to file.")


def find_student():
    student_id = input("Enter Student ID to search: ")

    if student_id in students:
        print("Student found:", students[student_id]["name"])
    else:
        print("Student not found.")


# ==============================
# MAIN PROGRAM
# ==============================

def main():
    load_from_file()

    while True:
        print("\n===== SAMSS MENU =====")
        print("1. Register Student")
        print("2. Record Academic Data")
        print("3. Update Fees")
        print("4. Display Student Report")
        print("5. Search Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register_student()

        elif choice == "2":
            record_academic_data()

        elif choice == "3":
            update_fees()

        elif choice == "4":
            display_student()

        elif choice == "5":
            find_student()

        elif choice == "6":
            print("Exiting system...")
            break

        else:
            print("Invalid choice.")


# Run program
main()