# 20. Creating a Custom Exception
# Assignment:
# Create a custom exception InvalidAgeError. 
# Write a function check_age(age) that raises this exception if age < 18.
# Handle it with try...except.


class InvalidAgeError(Exception):
    pass


def check_age(age):
    if age < 18:
        raise InvalidAgeError("Under 18 are not allow in this site 🔞")
    return f"{age}: valid age! walcome"


try:
    print(check_age(15))

except InvalidAgeError as a:
    print(f"Exception Caught: {a}", "  Exception Class Type: ", type(a))

    




