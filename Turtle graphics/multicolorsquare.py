import turtle            # set up alex
wn = turtle.Screen()
alex = turtle.Turtle()
alex.pensize(7)
for aColor in ["yellow", "red", "purple", "blue"]:
   alex.color(aColor)
   alex.forward(50)
   alex.left(90)

wn.exitonclick()
