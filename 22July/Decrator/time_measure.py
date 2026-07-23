import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Executed in {execution_time:.3f} seconds")
        return result

    return wrapper


@timer
def task1():
    print("Task1 started")
    time.sleep(5)
    print("Task1 finished")


task1()
