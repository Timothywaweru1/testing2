class Student:
    all = []
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self._teacher = None
        Student.all.append(self)

    @property
    def teacher(self):
        return self._teacher

    @teacher.setter
    def teacher(self,value):
        if not isinstance(value, Teacher):
            raise TypeError ("Teacher must be an instance of teacher class") 
        self._teacher = value

class Teacher:
    def __init__(self,name):
        self.name = name
    
    def students(self):
        return[student for student in Student.all if Student is self]