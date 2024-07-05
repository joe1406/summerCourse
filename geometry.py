import math

def sqr_perimeter():
    edge = int(input("what is the lenght of an edge: "))
    return edge**2

def circumference():
    r = int(input("what is the radius of your circle: "))
    circum2 = math.pi*r*2
    return circum2


perim = sqr_perimeter()
circum = circumference()

def compare():
    if perim > circum:
        print("nigga")


