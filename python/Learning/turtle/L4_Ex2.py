import turtle

def move_pen(x,y):
    my_ttl.penup()
    my_ttl.goto(x,y)
    my_ttl.pendown()

# set up screen
screen = 500
window = turtle.Screen()
window.setup(screen, screen)

# create turtle instance
my_ttl = turtle.Turtle()
my_ttl.shape("turtle")


def body():
    my_ttl.goto(-125,0)
    my_ttl.left(90)
    for _ in range(19):
        my_ttl.forward(5)
        my_ttl.left(10)
    my_ttl.goto(-200,0)
    my_ttl.goto(-200,100)
    my_ttl.goto(200,100)
    my_ttl.goto(200,0)
    my_ttl.goto(175,0)
    my_ttl.left(170)
    for _ in range(19):
        my_ttl.forward(5)
        my_ttl.left(10)
    my_ttl.goto(-125,0)
    
def wheel(x,y,a):
    move_pen(x,y)
    my_ttl.right(a)
    for _ in range(36):
        my_ttl.forward(5)
        my_ttl.left(10)

############################################
## Use you knowledge of Python and Turtle ##
## to draw a car. Use functions to ensure ##
## that you Do not Repeat Yourself.       ##
############################################

body()
wheel(-155,10,90)
wheel(145,10,0)
