import turtle 
ace = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor('lightgreen')
ace.pencolor('hotpink')
ace.pensize(3)
def drawPoly(someturtle, somesides, somesize):
    for i in range(somesides):
        someturtle.forward(somesize)
        someturtle.left(360/somesides)
        
print (drawPoly(ace, 8, 50))