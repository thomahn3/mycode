
import turtle

wn = turtle.Screen()
wn.setup(500, 500)
myTtl = turtle.Turtle()

######################################################
## Go Crazy and make something amazing with loops!! ##
######################################################

myTtl.speed(100)

for _ in range(360):
    myTtl.forward(100)
    myTtl.right(3)
    myTtl.backward(100)
    myTtl.left(6)

    