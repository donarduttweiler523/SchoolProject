def square_root(x):
    if x < 0:
        raise ValueError("Square root of negative number is not defined.")
    y = (x + 1) / 2
    while abs(y * y - x) > 1e-6:
        y = (y + x / y) / 2
    return y

print(square_root(4))
