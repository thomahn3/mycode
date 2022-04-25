
import turtle

wn = turtle.Screen()
wn.setup(500, 500)
myTtl = turtle.Turtle()

################################
## Draw a Triangle in 3 lines ##
################################

for _ in range(3):
    myTtl.forward(100)
    myTtl.right(120)