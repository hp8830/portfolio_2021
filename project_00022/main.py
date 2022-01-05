from random import randint
from app import GuiRectangle, GuiPoint, Point, Rectangle
import turtle

#Create an object 
rectangle = Rectangle(
    Point(randint(0,500), randint(0,500)),
    Point(randint(10,500), randint(10,500))
)

gui_rectangle = GuiRectangle(
    Point(randint(0,500), randint(0,500)),
    Point(randint(10,500), randint(10,500))
)

myturtle = turtle.Turtle()

gui_rectangle.draw(canvas=myturtle)
print(gui_rectangle.area())

#Print Rectangle Coordinates 
print("Rectangle coordinates: ",
gui_rectangle.point1.x, ",",
gui_rectangle.point1.y, ",",
gui_rectangle.point2.x, ",",
gui_rectangle.point2.y)


#Get point and area from user
user_point = GuiPoint(float(input("Guess X: ")), float(input("Guess y: ")))

user_area = float(input("Guess rectangle area: "))

#Print out the game results

print("Your point was inside the rectangle", user_point.falls_in_rectangle(gui_rectangle))


print("Your area was off by: ", gui_rectangle.area() - user_area)


gui_rectangle.draw(canvas=myturtle)
user_point.draw(canvas=myturtle)