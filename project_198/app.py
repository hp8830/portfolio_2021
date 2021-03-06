#Point in a rectangle
class Point: 

    def __init__(self, x, y):
        self.x = x
        self.y = y 

    def falls_in_rectangle(self, rectangle):
        if rectangle.lowleft.x < self.x < rectangle.upright.x \
        and rectangle.lowleft.y < self.y < rectangle.upright.y: 
            return True
        else: 
            return False

pointx = Point(6,7)

class Rectangle: 

    def __init__(self, lowleft, upright):
        self.lowleft = lowleft
        self.upright = upright

rectanglex = Rectangle(Point(5,6), Point(7,9))
print(pointx.falls_in_rectangle(rectanglex))


