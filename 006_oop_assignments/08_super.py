# 8. The super() Function
# Assignment:
# Create a class Person with a constructor that sets the name.
#Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.

class Person:
    def __init__(self,name):
        self.name =name


class Teacher(Person):
    def __init__(self, name,subject_field):
        self.subject_field = subject_field
        super().__init__(name) 


teacher = Teacher("Anwer", "Math")  # who can forget sir Anwer
print(teacher.name)          
print(teacher.subject_field) 