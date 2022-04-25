
import turtle

wn = turtle.Screen()
wn.setup(500, 500)
myTtl = turtle.Turtle()

###############################
## Draw a Hexagon in 3 lines ##
###############################

for _ in range(6):
    myTtl.forward(100)
    myTtl.right(60)