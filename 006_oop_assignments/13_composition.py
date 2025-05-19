# 13. Composition
# Assignment:
# Create a class Engine and a class Car.
# Use composition by passing an Engine object to the Car class during initialization.
# Access a method of the Engine class via the Car class.

class Engine:
    def __init__(self):
          pass #i dont know even know C or Car what can i write in Engine TT
    
    def engine_start(self):
         return f"________ Engine started..... car is ready to be drived"
    
class Car:
    engine:Engine
    def __init__(self,engine):
         self.engine = engine

    def start_car(self):
        return self.engine.engine_start()


engine = Engine()
car = Car(engine)
print(car.start_car())
