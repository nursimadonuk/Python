import turtle
n = str(input("what would you like the window color to be?"))

wn = turtle.Screen()
wn.bgcolor(n)                   # set the window background color to n

tc = str(input("what would you like the turtle color to be?"))
tess = turtle.Turtle()
tess.color(tc)                  # make tess color the input
ps = int(input("what would you like the pen width to be?"))
tess.pensize(ps)                 # set the width of her pen
side = int(input("How long would you like the triangle's side to be?"))
tess.forward(side)
tess.left(120)
tess.forward(side)
tess.left(120)
tess.forward(side)

wn.exitonclick()                # wait for a user click on the canvas
