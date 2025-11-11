class Parent:
    def s_p(self):
        print("These is a parent class")
        
class Child(Parent):
    def s_c(self):
        print("These is a child class ")

obj=Child()
obj.s_p()
obj.s_c()