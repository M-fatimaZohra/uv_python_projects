# 18. Property Decorators: @property, @setter, and @deleter
# Assignment:
# Create a class Product with a private attribute _price. 
# Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.


class Product:
    def __init__(self,price):
        self.__price = price

    
    @property
    def price(self):
        return self.__price
    
       
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value

    @price.deleter
    def price(self):
        del self.__price
        print("deleted")
        


cash = Product(100)
print(cash.price)

cash.price += 150
print(cash.price)

del cash.price









