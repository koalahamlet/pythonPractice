
import turtle
import math
import random


fred = turtle.Turtle()

wn = turtle.Screen()
wn.setworldcoordinates(-1,-1,1,1)
fred.penup()
fred.tracer(100)
numdarts = 5000
incircle = 0
for i in range(numdarts):
    randx = random.random()
    randy = random.random()
    x =randx*2-1
    y =randy*2-1
    fred.goto(x,y)
    if fred.distance(0,0)>1:
      fred.color("red")
      fred.dot()
    else:
      incircle = incircle + 1
      fred.color("blue")
      fred.dot()

print(incircle, "hits")
pi = (float(incircle)/float(numdarts))*4 #Monte Carlo estimate of pi
print(pi, "is pi")
wn.exitonclick()
