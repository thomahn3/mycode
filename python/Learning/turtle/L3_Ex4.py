import turtle

def movepen(x, y):
    my_ttl.penup()
    my_ttl.goto(x, y)
    my_ttl.pendown()

# set up screen
screen = 500
window = turtle.Screen()
window.setup(screen, screen)

# create turtle instance
my_ttl = turtle.Turtle()

##################################
## Using the tutrle command you ##
## have learnt, draw a house.   ##
##################################

movepen(0,0)

for i in range(4):
    my_ttl.forward(100)
    my_ttl.left(90)

movepen(0,100)

for i in range(3):
    my_ttl.forward(100)
    my_ttl.left(120)

movepen(50,0)

for i in range(2):
    my_ttl.forward(25)
    my_ttl.left(90)
    my_ttl.forward(50)
    my_ttl.left(90)