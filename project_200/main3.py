from app import Point, Rectangle
from random import randint

rectangle = Rectangle(
    Point(randint(3,7), randint(4,8)),
    Point(randint(9, 15), randint(9, 15))
)

user_point = Point(float(input("Guess X: ")),
                float(input("Guess Y: ")))

user_area = float(input("Guess rectangle area: "))

print("Your point was inside rectangle: ", 
    user_point.falls_in_rectangle(rectangle))

print("Your point was outside rectangle: ", 
    user_point.falls_out_rectangle(rectangle))

print("Your area was off by rectangle: ", 
    rectangle.area() - user_area)