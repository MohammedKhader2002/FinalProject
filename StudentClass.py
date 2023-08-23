from CourseClass import Course


class Student:
    counter = 1

    def __init__(self, name, level, courses, ):
        self.id = Student.counter
        Student.counter += 1
        self.name = name
        self.level = level
        self.courses = courses

    # Method to add new student
    def Add_new_student(self):
        self.name = input("Enter student name: ")
        self.level = input("Select your level (A,B,C): ")

        if self.level == "A" or self.level == "B" or self.level == "C" or self.level == "a" or self.level == "b" or self.level == "c":
            print("student saved successfully")

        else:
            print("try again")
            std_ob.Add_new_student()

    # Method to remove student
    def Remove_student(self):

        std_id = str(input("Enter student id please :"))

        if std_id in str(self.id):
            print("Delete done successful")

        else:
            print("User not exist")

    # Method to edit student
    def Edit_student(self):

        std_id = str(input("Enter student id please :"))

        if std_id not in str(self.id):
            print("User not exist")

        else:
            self.name = input("Enter new name: ")
            self.level = input("select new level(A,B,C): ")

            if self.level == "A" or self.level == "B" or self.level == "C" or self.level == "a" or self.level == "b" or self.level == "c":
                print("student saved successfully")

            else:
                print("try again")
                std_ob.Edit_student()

    # Method to display all students
    def Display_all_students(self):
        print(
            f"Student name is {self.name}\nStudent id is:{self.id}\nStudent level is:{self.level}\nStudent courses is:{self.courses} ")

    # Method to add course to student
    def Add_course_to_student(self):

        student_id = str(input("Enter your id: "))

        if student_id in str(self.id):
            course_id = str(input("Enter course id"))
            if course_id in str(Course.counter):
                print("done")
            else:
                print("course not exist")

        else:
            print("You are not student")


std_ob = Student("mohammed", "c", "artificial intelligence")
