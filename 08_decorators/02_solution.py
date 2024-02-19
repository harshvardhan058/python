def debugger(func):
    def wrapper(*args,**kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{key}={value}" for key,value in kwargs.items())
        print(f"calling {func.__name__} with args {args_value} and kwargs {kwargs_value} ")
        return func(*args,**kwargs)
    return wrapper

@debugger
def multiple_table(n):
    for i in range(1,11):
        print(f"{n} * {i} = {n*i}")

@debugger
def greet(name,greeting="Namaste"):
    print(f"{greeting}, {name}")


multiple_table(13)
greet("Harshvardhan","Vadakam")