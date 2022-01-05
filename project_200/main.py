from random import randint 
from app import Point, Rectangle

rectangle = Rectangle(
    Point(randint(0,9), randint(0,9)),
    Point(randint(10,19), randint(10,19))
)

print( "Rectangle Coordinates:",
rectangle.lowleft.x, ",", 
rectangle.lowleft.y, "and ", 
rectangle.upright.x, ",",
rectangle.upright.y)

