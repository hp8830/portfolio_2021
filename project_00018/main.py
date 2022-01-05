import turtle
#Create a canvas instance
myturtle = turtle.Turtle()
#go to a certain coordinate
myturtle.penup()
myturtle.goto(0,0)
myturtle.pendown()

myturtle.color("#ECDBBA","#ECDBBA" )
myturtle.begin_fill()
myturtle.circle(200,180)
myturtle.end_fill()

myturtle.penup()
myturtle.goto(0,0)
myturtle.pendown()

myturtle.color("#ECDBBA","#ECDBBA" )
myturtle.begin_fill()
myturtle.circle(150, 180)
myturtle.end_fill()


turtle.done()