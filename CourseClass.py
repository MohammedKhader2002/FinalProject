class Course:
    counter = 1

    def __init__(self, name, level):
        self.id = Course.counter
        Course.counter += 1
        self.name = name
        self.level = level

    # Method to create new course
    def Create_new_course(self):
        self.name = input("please enter your class name: ")
        self.level = input("Please enter your level(A,B,C): ")

        if self.level == "A" or self.level == "B" or self.level == "C" or self.level == "a" or self.level == "b" or self.level == "c":
            print("student saved successfully")

        else:
            print("try again")
            cou_obj.Create_new_course()


cou_obj = Course("system analysis", "B")