class Student:
    def __init__(self, student_id, name, age, course, email):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.email = email

    def display(self):
        print("\n--- Student Details ---")
        print("Student ID :", self.student_id)
        print("Name       :", self.name)
        print("Age        :", self.age)
        print("Course     :", self.course)
        print("Email      :", self.email)


class StudentManagement:
    def __init__(self):
        self.students = []

    def add_student(self):
        student_id = input("Enter Student ID: ")
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        course = input("Enter Course: ")
        email = input("Enter Email: ")

        student = Student(student_id, name, age, course, email)
        self.students.append(student)

        print("\nStudent added successfully!")

    def display_students(self):
        if not self.students:
            print("\nNo students found.")
            return

        print("\n===== All Students =====")

        for student in self.students:
            student.display()

    def search_student(self):
        student_id = input("Enter Student ID to search: ")

        for student in self.students:
            if student.student_id == student_id:
                student.display()
                return

        print("\nStudent not found.")

    def delete_student(self):
        student_id = input("Enter Student ID to delete: ")

        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print("\nStudent deleted successfully!")
                return

        print("\nStudent not found.")

    def update_student(self):
        student_id = input("Enter Student ID to update: ")

        for student in self.students:
            if student.student_id == student_id:

                student.name = input("Enter New Name: ")
                student.age = int(input("Enter New Age: "))
                student.course = input("Enter New Course: ")
                student.email = input("Enter New Email: ")

                print("\nStudent updated successfully!")
                return

        print("\nStudent not found.")


# Create object of StudentManagement
system = StudentManagement()


while True:

    print("\n==============================")
    print("     STUDENT MANAGEMENT SYSTEM")
    print("==============================")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    print("==============================")

    choice = input("Enter your choice: ")

    if choice == "1":
        system.add_student()

    elif choice == "2":
        system.display_students()

    elif choice == "3":
        system.search_student()

    elif choice == "4":
        system.update_student()

    elif choice == "5":
        system.delete_student()

    elif choice == "6":
        print("\nThank you for using Student Management System!")
        break

    else:
        print("\nInvalid choice. Please try again.")