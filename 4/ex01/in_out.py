def square(x: int | float) -> int | float:
    return x ** 2

def pow(x: int | float) -> int | float:
    return x ** x

def outer(x: int | float, function) -> object:
    count = float(x)  # store as float for precision

    def inner():
        nonlocal count
        count = function(count)
        return count

    return inner
