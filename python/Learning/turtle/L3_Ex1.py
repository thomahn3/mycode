import turtle

#################################################
## Change the variable values to draw a square ##
#################################################

screen = 500
sides = 4
length = 100

# window = turtle.Screen()
# window.setup(screen, screen)
# my_ttl = turtle.Turtle()

for i in range(sides):
    turtle.forward(length)
    turtle.left(360 / sides)