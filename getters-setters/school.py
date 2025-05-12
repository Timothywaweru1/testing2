class Student:
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks

class Course:
    def __init__(self,course_name):
        self.course_name = course_name
        self.students = []
    def add_student(self,student):
        self.students.append(student)                  
    def course_average(self):
        count = 0 
        for student in self.students:
            count += student.marks
            print(count / len(self.students))           
student_1 = Student("Tom",10,79)
student_2 = Student("Mary",11,81)
student_3 = Student("Brad",12,85)
c = Course("Python")
c.add_student (student_1)
c.add_student (student_2)
c.add_student (student_3)


c.course_average()