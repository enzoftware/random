import turtle
wn = turtle.Screen()
kath = turtle.Turtle()
kath.pensize(6)
kath.penup()
kath.shape("turtle")
kath.color("pink")
for size in range(10):
    kath.forward(50)
    kath.stamp()
    kath.forward(-50)
    kath.right(36) # 36 * 10 = 360 grades 

turtle.exitonclick()
