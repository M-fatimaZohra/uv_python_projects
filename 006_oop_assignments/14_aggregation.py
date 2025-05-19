# 14. Aggregation
# Assignment:
# Create a class Department and a class Employee. 
# Use aggregation by having a Department object store 
# a reference to an Employee object that exists independently of it.


class Department:
      def __init__(self, name, employee):
        self.name = name
        self.employee = employee

class Employee:
    def __init__(self,name):
        self.name = name


employ_1 = Employee("Zayne")
print(employ_1.name)
hospital_department = Department("Cardiac department", employ_1)

print(hospital_department.employee.name)
print(hospital_department.name)