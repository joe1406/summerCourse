import math

w = int(input("what is the lenght of one side? "))
h = int(input("what is the lenght of the other side? "))

print(f"the area of the rectangle is {w*h}")

r = int(input("what is the radius of the circle? "))

print(f"the area of the circle is: {math.pi*r**2}")

b = int(input("what is the lenght of the base of the triangle? "))
height = int(input("what is the height of the triangle? "))
print(f"the area of the triangle is {0.5*b*height}")