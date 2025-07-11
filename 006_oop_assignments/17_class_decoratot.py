# 17. Class Decorators
# Assignment:
# Create a class decorator add_greeting that modifies a class to add a greet()
# method returning "Hello from Decorator!". Apply it to a class Person.




        
def add_greeting(cls):
    def greet(cls):
        return "Hello from Decorator!"
    
    cls.greet = greet  
    return cls

@add_greeting
class Person:
    def __init__(self):
        pass

person = Person()
print(person.greet())  #the reason it is not showing as method but working perfectly is because Vs IDE can not predict dynamic flow
