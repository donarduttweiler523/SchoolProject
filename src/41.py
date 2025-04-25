import math

def calculate_volume_cylinder(radius: float, height: float) -> float:
    """
    Calculate the volume of a cylinder.
    
    Args:
        radius (float): The radius of the cylinder's base.
        height (float): The height of the cylinder.
        
    Returns:
        float: The volume of the cylinder.
    """
    return math.pi * radius ** 2 * height

def main() -> None:
    print("Volume of a cylinder with radius 5.0 and height 10.0 is {:.2f} square units.".format(calculate_volume_cylinder(5.0, 10.0)))

if __name__ == "__main__":
    main()
