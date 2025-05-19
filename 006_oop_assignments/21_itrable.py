# 21. Make a Custom Class Iterable
# Assignment:
# Create a class Countdown that takes a start number. 
# Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0.


import time

class Countdown:
    def __init__(self, num):
        self.num = num

    def __iter__(self):
        return self 

    def __next__(self):
        if self.num < 0:
            raise StopIteration
        time.sleep(0.5)
        given_number = self.num
        self.num -= 1
        return given_number 




for number in Countdown(199):
    print(number)
