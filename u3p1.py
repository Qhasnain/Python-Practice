class Student:
    def __init__(self,name,rollno,course,age):
        self.name=name
        self.rollno=rollno
        self.course=course
        self.age=age
    
    def display(self):
        print("Name :",self.name)
        print("Roll no  :",self.rollno)
        print("Course :",self.course)
        print("Age :",self.age)
        
s1=Student("Hasnain",131,"BCA",18)
s2=Student("Meet",164,"BCA",18)

s1.display()
s2.display()
        