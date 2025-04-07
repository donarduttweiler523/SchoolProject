import math

def calculate_area(shape, dimensions):
    if shape == "rectangle":
        length = dimensions[0]
        width = dimensions[1]
        area = length * width
    elif shape == "circle":
        radius = dimensions[0] / 2
        area = math.pi * (radius ** 2)
    else:
        raise ValueError("Unsupported shape")
    return area

# Example usage:
shapes = ["rectangle", "circle", "triangle"]
dimensions = [4, 6, 3]
print(calculate_area("rectangle", dimensions))
