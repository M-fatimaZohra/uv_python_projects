# 19. callable() and __call__()
# Assignment:
# Create a class Multiplier with an __init__() to set a factor. 
# Define a __call__() method that multiplies an input by the factor. 
# Test it with callable() and by calling the object like a function.

class Multiplier:
    def __init__(self,factor):
        self.factor = factor

    def __call__(self,input ):

        return input * self.factor
    

multi = Multiplier(4)

print(callable(multi))
print(multi(2))
        
        

