#Creating a class and method, practice 
from typing import Match


class Point: 

    def __init__(self, x, y):
        self.x = x
        self.y = y 

    def falls_in_rectangle(self, lowleft, upright):
        if lowleft[0] < self.x < upright[0] \
        and lowleft[1] < self.y < upright[1]:
            return True

        else: 
            return False

    def distance_from_point(self, x, y):
        return ((self.x -x)**2 + (self.y - y)**2) **0.5

point1 = Point(7,8)

print(point1.x, point1.y)
print(point1.distance_from_point(5,9))
