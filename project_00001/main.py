from random import randint
from app import Point, Rectangle

#Create an object 
rectanglex = Rectangle(
    Point(randint(0,500), randint(0,500)),
    Point(randint(10,500), randint(10,500))
)

#Print Rectangle Coordinates 
print("Rectangle coordinates: ",
rectanglex.point1.x, ",",
rectanglex.point1.y, ",",
rectanglex.point2.x, ",",
rectanglex.point2.y)


#Get point and area from user
user_point = Point(float(input("Guess X: ")), float(input("Guess y: ")))

user_area = float(input("Guess rectangle area: "))

#Print out the game results

print("Your point was inside the rectangle", user_point.falls_in_rectangle(rectanglex))
print("Your area was off by: ", rectanglex.area() - user_area)

