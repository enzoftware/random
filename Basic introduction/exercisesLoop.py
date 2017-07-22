import turtle
### EXERCISE N# 1 ###
## Write a program that prints We like Python's turtles! 100 times. ##
for i in range(100):
    print("We like python turtles")

### EXERCISE N# 2 ###
#Write a program that uses a for loop to print
#One of the months of the year is January
#One of the months of the year is February
#One of the months of the year is March
#etc ...

for i in ["jan","feb","mar","apr","may","jun","jul","agos","sept","oct","nov","dic"]:
    print("One of the months of the year is ",i)


### EXERCISE N#3 ###
#Use for loops to make a turtle draw these regular polygons
#(regular means all sides the same lengths, all angles the same):
#An equilateral triangle
#A square
#A hexagon (six sides)
#An octagon (eight sides)

wn = turtle.Screen()

##TRIANGLE
t = turtle.Turtle()
t.color("blue")
for i in range(3):
    t.forward(150)
    t.left(120)

##SQUARE

sq = turtle.Turtle()
sq.color("yellow")
for i in range(4):
    sq.forward(100)
    sq.left(90)

## HEXAGON

hx = turtle.Turtle()
hx.color("red")
for i in range(6):
    hx.forward(80)
    hx.left(60)

## OCTAGON

hx = turtle.Turtle()
hx.color("green")
for i in range(8):
    hx.forward(80)
    hx.left(45)





### EXERCISE N#4 ###
#Write a program that asks the user for the number of sides,
#the length of the side, the color.
#The program should draw the polygon and then fill it in.
ns = int(input("Enter the number of sides : "))
l = int(input("Enter the lenght of the side : "))
color = str(input("Enter the color : "))

pencil = turtle.Turtle()
pencil.color(color)
pencil.pensize(6)

for i in range(ns):
    pencil.forward(l)
    pencil.left(360/ns)


wn.exitonclick()
