# 7. Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.




class Employee:
    def __init__(self,name,salary,ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn



ali = Employee("Ali",50000,"372-54-8190")

print(ali.name)
print(ali._salary)
print(ali.__ssn)




# In terminal
# Ali
# 50000
# Traceback (most recent call last):
# File "C:\file_test\07_access.py", line 28, in <module>
#    print(ali.__ssn)
#           ^^^^^^^^^
# AttributeError: 'Employee' object has no attribute '__ssn'


# here it make __ssn  non accessable out side class