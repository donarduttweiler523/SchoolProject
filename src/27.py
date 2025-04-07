def square_root(x):
    if x < 0:
        raise ValueError("Cannot find square root of a negative number")
    
    y = x / 2.0
    
    while True:
        y = (y + x / y) / 2.0
        if abs(y - x / y) < 1e-6:
            return y

try:
    print(square_root(-4))
except ValueError as e:
    print(e)
