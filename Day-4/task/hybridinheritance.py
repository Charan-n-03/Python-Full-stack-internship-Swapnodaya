class Person:
    def __init__(self,name):
        self.name=name

    def display_person(self):
        print("Person:",self.name)

class Student(Person):
    def __init__(self,student_id,name):
        Person.__init__(self,name)
        self.student_id = student_id

    def display_student(self):
        print("ID:",self.student_id)
        print("Name:",self.name)

class SportsPlayer(Person):
    def __init__(self,sport_name,name):
        Person.__init__(self,name)
        self.sport_name=sport_name

    def display_sports_player(self):
        print(self.name,"plays ",self.sport_name)

class CollegeStudent(Student,SportsPlayer):
    def __init__(self,college_name,name,student_id,sport_name):
        Student.__init__(self,student_id,name)
        SportsPlayer.__init__(self,sport_name,name)
        self.college_name=college_name

    def display_college_student(self):
        print("College:",self.college_name)
        print("Name:",self.name)
        print("ID:",self.student_id)
        print("He plays:",self.sport_name)
        
S1 = CollegeStudent("GECR","Charan","1GG22CS014","Football")
S1.display_college_student()