import turtle

turing = turtle.Turtle()
wn = turtle.Screen()

turing.begin_fill()

for i in range(5):
    turing.forward(110)
    turing.left(216)

turing.end_fill()

wn.exitonclick()