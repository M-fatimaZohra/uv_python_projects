# 15. Method Resolution Order (MRO) and Diamond Inheritance
# Assignment:
# Create four classes:

# A with a method show(),

# B and C that inherit from A and override show(),

# D that inherits from both B and C.

# Create an object of D and call show() to observe MRO.


class  A:
    def __init__(self):
        pass

    def show(self):
        return "Real life doesn't always have happy endings. However... with you here, my story won't end in tragedy."

class B(A):
    def __init__(self):
        super().__init__()
    def show(self):
        return "If I lose my sight one day, I'll be counting on you to see the world for me."

class C(A):
    def __init__(self):
        super().__init__()
    def show(self):
        return "From stars we rise, to stars we fall..One day we will meet under the stars again."




class D(B,C):
    def __init__(self):
        super().__init__()



test_4_mro = D()

print(test_4_mro.show())

#Terminal
# If I lose my sight one day, I'll be counting on you to see the world for me.