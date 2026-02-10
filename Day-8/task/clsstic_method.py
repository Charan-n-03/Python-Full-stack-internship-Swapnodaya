class Student:
    college_name = "ABC College"   # class variable

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"College: {Student.college_name}")
        print("-------------------")

    @classmethod
    def change_college(cls, new_name):
        cls.college_name = new_name

    @staticmethod
    def is_pass(marks):
        if marks >= 35:
            return "Pass"
        else:
            return "Fail"


# Testing
s1 = Student("Rahul", 1)
s2 = Student("Anita", 2)

s1.display()
s2.display()

# Change college for all students
Student.change_college("XYZ College")

s1.display()
s2.display()

# Static method test
print(Student.is_pass(40))
print(Student.is_pass(20))
