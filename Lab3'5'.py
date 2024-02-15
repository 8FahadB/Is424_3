def repeat_decorator(num_repetitions):
    def decorator(func):
        def wrapper():
            for _ in range(num_repetitions):
                func()
        return wrapper
    return decorator

x = int(input("Enter a number of repetitions: "))

@repeat_decorator(x)
def hello():
    print("Hello")

hello()
