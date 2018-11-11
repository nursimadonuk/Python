import turtle
wn = turtle.Screen()
sam = turtle.Turtle()
sam.pencolor('hotpink')
wn.bgcolor('lightgreen')
sam.pensize(3)

def drawsquare(t , size):
    for i in range (4):
        t.forward(size)
        t.left(90)
    return 
     
def turn():
    sam.left(180)
    sam.up()
    sam.forward(10)
    sam.left(90)
    sam.forward(10)
    sam.left(90)
    sam.down()
for sz in [ 20, 40, 60, 80]:
    print (drawsquare(sam, sz)) 
    print (turn())
    
wn.exitonclick()

