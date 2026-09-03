import json
import os

DATA_FILE = "students.json"


def load_students():
    """Load student data from JSON file."""
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_students(students):
    """Save student data to JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(students, file, indent=4)


def calculate_average(marks):
    return sum(marks) / len(marks)


def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def get_marks():
    """Get five subject marks from the user."""
    marks = []

    for i in range(1, 6):
        while True:
            try:
                mark = float(input(f"Enter marks for Subject {i} (0-100): "))

                if 0 <= mark <= 100:
                    marks.append(mark)
                    break

                print("Marks must be between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")

    return marks


def add_student(students):
    student_id = input("Enter student ID: ").strip()

    if any(student["id"] == student_id for student in students):
        print("Student ID already exists.")
        return

    name = input("Enter student name: ").strip()
    course = input("Enter course: ").strip()

    if not name or not course:
        print("Name and course cannot be empty.")
        return

    marks = get_marks()

    average = calculate_average(marks)
    grade = calculate_grade(average)

    student = {
        "id": student_id,
        "name": name,
        "course": course,
        "marks": marks,
        "average": round(average, 2),
        "grade": grade
    }

    students.append(student)
    save_students(students)

    print("\nStudent added successfully!")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")


def display_student(student):
    print("\n----------------------------")
    print(f"ID      : {student['id']}")
    print(f"Name    : {student['name']}")
    print(f"Course  : {student['course']}")
    print(f"Marks   : {student['marks']}")
    print(f"Average : {student['average']}")
    print(f"Grade   : {student['grade']}")
    print("----------------------------")


def view_students(students):
    if not students:
        print("No students found.")
        return

    print(f"\nTotal Students: {len(students)}")

    for student in students:
        display_student(student)


def search_student(students):
    student_id = input("Enter student ID to search: ").strip()

    for student in students:
        if student["id"] == student_id:
            display_student(student)
            return

    print("Student not found.")


def update_student(students):
    student_id = input("Enter student ID to update: ").strip()

    for student in students:
        if student["id"] == student_id:
            print("\nLeave the field empty to keep the existing value.")

            name = input(f"Name [{student['name']}]: ").strip()
            course = input(f"Course [{student['course']}]: ").strip()

            if name:
                student["name"] = name

            if course:
                student["course"] = course

            choice = input("Update marks? (y/n): ").lower()

            if choice == "y":
                student["marks"] = get_marks()
                average = calculate_average(student["marks"])
                student["average"] = round(average, 2)
                student["grade"] = calculate_grade(average)

            save_students(students)
            print("Student updated successfully.")
            return

    print("Student not found.")


def delete_student(students):
    student_id = input("Enter student ID to delete: ").strip()

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            save_students(students)
            print("Student deleted successfully.")
            return

    print("Student not found.")


def show_top_student(students):
    if not students:
        print("No students available.")
        return

    top_student = max(students, key=lambda student: student["average"])

    print("\nTop Performing Student")
    display_student(top_student)


def menu():
    students = load_students()

    while True:
        print("\n================================")
        print("     STUDENT MANAGEMENT SYSTEM")
        print("================================")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Show Top Student")
        print("7. Exit")
        print("================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student(students)

        elif choice == "2":
            view_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            update_student(students)

        elif choice == "5":
            delete_student(students)

        elif choice == "6":
            show_top_student(students)

        elif choice == "7":
            print("Thank you for using Student Management System!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()