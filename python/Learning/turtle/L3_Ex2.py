import turtle

#################################################
## Change the variable values to draw a circle ##
#################################################

screen = 500
sides = 6
length = 100

turtle.screensize(500,500)
my_ttl = turtle.Turtle()

for i in range(sides):
    my_ttl.forward(length)
    my_ttl.left(360 / sides)