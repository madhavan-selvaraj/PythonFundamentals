def execution_logger(func):
    def wrapper(*args, **kwargs):
        print("Function started")
        result = func(*args, **kwargs)
        print("Function finished")
        return result

    return wrapper


@execution_logger
def greet(name):
    print(f"Hello {name}")


@execution_logger
def add(a, b):
    print(f"Sum = {a + b}")


@execution_logger
def display():
    print("This is Execution Log ")


greet("Ram")
print()

print(add(10, 2))

print(display())
