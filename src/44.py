import math

def calculate_surface_area(radius):
    area = math.pi * radius ** 2
    return area

radius = 5  # Example: The radius of the circle (for example a circle with a radius of 5 units)
area = calculate_surface_area(radius)

print(f"The surface area is {area:.2f} square units.")
