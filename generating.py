from random import randint

def generate_dataset(size, start, end):
    return [randint(start, end) for _ in range(size)]

