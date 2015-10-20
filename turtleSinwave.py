import math
import turtle

wn = turtle.Screen()
wn.bgcolor('lightblue')
wn.setworldcoordinates(-50,-50,400,50)

fred = turtle.Turtle()
fred.color("blue")

for angle in range(360):
    y = math.sin(math.radians(angle))
    fred.goto(angle, y*50)

wn.exitonclick()
