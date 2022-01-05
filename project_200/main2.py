from app import Point, Rectangle
from random import randint

rectangle = Rectangle(
    Point(randint(3,7), randint(4,8)),
    Point(randint(9, 15), randint(9, 15))
)

user_point = Point(float(input("Guess X: ")),
                float(input("Guess Y: ")))

print("Your point was inside rectangle: ", 
    user_point.falls_in_rectangle(rectangle))