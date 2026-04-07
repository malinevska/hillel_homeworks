import functools

# 1.1 Generator of even numbers from 0 to N:
def even_generator(number):
    for i in range(0, number + 1, 2):
        yield i

# 1.2 Fibonacci sequence generator up to a given number N:
def fibonacci_generator(number):
    a, b = 0, 1
    while a <= number:
        yield a
        a, b = b, a + b

# 2.1 Iterator to yield list elements in reverse:
class ReverseIterator:
    def __init__(self, data_list):
        self.data_list = data_list
        self.index = len(data_list)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data_list[self.index]

# 2.2 Iterator for even numbers in the range from 0 to N:
class EvenIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration

        value = self.current
        self.current += 2
        return value

# 3.1 Decorator for logging arguments and results:
def log_function(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Call of function '{func.__name__}' with arguments: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] Function '{func.__name__}' returned: {result}")
        return result
    return wrapper

# 3.2 Decorator for intercepting and handling exceptions:
def handle_exceptions(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"[ERROR] Error occurred '{func.__name__}': {e}")
            return None
    return wrapper