from math import pi

def square_footage(length, width):
    if not isinstance(width,(float,int)):
        return "input values are not valid"
    elif not isinstance(length,(float,int)):
        return "input values are not valid"
    elif length < 0 or width < 0:
        return "Can't have negative lengths of sides"
    return f'{length*width} length units squared'

def circumference(radius):
    if not isinstance(radius,(float,int)):
        return "input radius is not valid"
    elif radius < 0:
        return "Can't have a negative radius length"
    return f'{2*pi*radius} length units'