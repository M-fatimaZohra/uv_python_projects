# 16. Function Decorators
# Assignment:
# Write a decorator function log_function_call that prints "Function is being called"
# before a function executes. Apply it to a function say_hello().

def log_function_call(func):
    def write():
        print("Function is being called")
        func()

    return write


@log_function_call
def say_hello():
    print("Hello!")

say_hello()