import turtle

def draw_rectangle(hor,vert):
    for i in range(2):
        my_ttl.forward(hor)
        my_ttl.left(90)
        my_ttl.forward(vert)
        my_ttl.left(90)

# set up screen
screen = 500
window = turtle.Screen()
window.setup(screen, screen)

# create turtle instance
my_ttl = turtle.Turtle()
my_ttl.shape("arrow")

##################################
## Using the tutrle command you ##
## have learnt, draw a house.   ##
##################################

# move pen
my_ttl.penup()
my_ttl.goto(-100,0)
my_ttl.pendown()

# draw_square
for i in range(4):
    my_ttl.forward(200)
    my_ttl.right(360 / 4)

# draw_triangle
for i in range(3):
    my_ttl.forward(200)
    my_ttl.left(120)

# move pen
my_ttl.penup()
my_ttl.goto(-25,-200)
my_ttl.pendown()

# draw rectangle
for i in range(2):
    my_ttl.forward(50)
    my_ttl.left(90)
    my_ttl.forward(100)
    my_ttl.left(90)

# move pen
my_ttl.penup()
my_ttl.goto(-80,-100)
my_ttl.pendown()

# draw_square
for i in range(4):
    my_ttl.forward(35)
    my_ttl.right(360 / 4)

# move pen
my_ttl.penup()
my_ttl.goto(45,-100)
my_ttl.pendown()

# draw_square
for i in range(4):
    my_ttl.forward(35)
    my_ttl.right(360 / 4)

# move pen
my_ttl.penup()
my_ttl.goto(15,-150)
my_ttl.pendown()
my_ttl.circle(5)
my_ttl.hideturtle()