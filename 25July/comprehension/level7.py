# Create a generator that yields the squares of numbers from 1 to 10.
def square_generator():
    for i in range(1, 11):
        yield i**2


for square in square_generator():
    print(square)


# Create a generator that yields only even numbers from 1 to 20.
def even_num():
    for num in range(1, 21):
        if num % 2 == 0:
            yield num


for num in even_num():
    print(num)
