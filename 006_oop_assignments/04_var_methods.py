# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name.
#  Add a class method change_bank_name(cls, name) that allows changing the bank name.
#  Show that it affects all instances.

class Bank:
    bank_name = "Al Habib"
    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name = name

        return cls.bank_name
    

bank = Bank()
print(bank.bank_name)
print(bank.change_bank_name('Allied Bank'))

