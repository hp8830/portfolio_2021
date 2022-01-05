import turtle

class Point:

    def __init__(self, x,y):
        self.x = x
        self.y = y 

    def falls_in_rectangle(self, rectangle):
        if rectangle.point1.x < self.x < rectangle.point2.x \
        and rectangle.point1.y > self.y < rectangle.point2.y:
            return True
        else:
            return False

class Rectangle:

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return (self.point2.x - self.point1.x) * (self.point2.y - self.point1.y)

class GuiRectangle(Rectangle):
    def draw(self, canvas):
        canvas.penup()
        canvas.goto(self.point1.x, self.point1.y)
        canvas.pendown()
        
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)

        

class GuiPoint(Point):

    def draw(self, canvas, size=3, color="#32502E"):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()

        canvas.dot(size, color)
        
        turtle.done()