# محمد محمود خضر
from StudentClass import Student
from CourseClass import Course

obj_course = Course("data base", "A")
obj_student = Student("ali", "B", "data base")

Main_Page = input(
    "Select Choice Please\n 1.Add New Student\n 2.Remove Student\n 3.Edit Student\n 4.Display All Students\n 5.Create "
    "New Course\n 6.Add course to student\n 0.Exit\n")

if Main_Page == "1":

    obj_student.Add_new_student()



elif Main_Page == "2":

    obj_student.Remove_student()


elif Main_Page == "3":

    obj_student.Edit_student()


elif Main_Page == "4":

    obj_student.Display_all_students()

elif Main_Page == "5":

    obj_course.Create_new_course()


elif Main_Page == "6":
    obj_student.Add_course_to_student()

else:
    print("Good luck !!")

