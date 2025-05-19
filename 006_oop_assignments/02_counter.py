# 2. Using cls
# Assignment:
# Create a class Counter that keeps track of how many objects have been created. 
# Use a class variable and a class method with cls to manage and display the count.

class Counter:
    length = 0
    def __init__(self):
        Counter.length += 1
    @classmethod
    def display(cls):
        return cls.length
    


obj1 = Counter()
obj2 = Counter()
obj3 = Counter()
obj4 = Counter()
obj5 = Counter()
print(Counter.display())