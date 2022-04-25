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

############################################
## Convert the code below using functions ##
############################################

# Move Pen
move_pen(0,-200)

# draw head
my_ttl.color("black","yellow")
my_ttl.begin_fill()
my_ttl.circle(200)
my_ttl.end_fill()

# move pen
move_pen(-75,0)

# draw eye
my_ttl.color("black","black")
my_ttl.begin_fill()
my_ttl.circle(50)
my_ttl.end_fill()

# move pen
move_pen(75,0)

# draw eye
my_ttl.color("black","black")
my_ttl.begin_fill()
my_ttl.circle(50)
my_ttl.end_fill()

# move pen
move_pen(-100,-75)

# draw mouth
my_ttl.color("black","black")
my_ttl.begin_fill()
for i in range(2):
    my_ttl.forward(200)
    my_ttl.right(90)
    my_ttl.forward(25)
    my_ttl.right(90)
my_ttl.end_fill()

my_ttl.hideturtle()