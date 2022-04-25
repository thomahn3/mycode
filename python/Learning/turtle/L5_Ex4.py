import turtle

def draw_poly(length, sides, color):
    fred.color("black",color)
    fred.begin_fill()
    for i in range(sides):
        fred.forward(length)
        fred.right(360/sides)
    fred.end_fill()

############################################
## adjust the get_number code so it loops ##
## until the user provides a valid input  ##
############################################

def get_number(prompt):
    while True:
        num = input(prompt)
        if num.lstrip("-").isdigit():
            return int(num)
        else:
            print("Invalid input")
        

###########################################
## adjust the get_color code so it loops ##
## until the user provides a valid input ##
###########################################

def get_color():
    color = input("Fill colour (red, blue, green)?> ").lower()
    if color == "red":
        return color
    elif color == "blue":
        return color
    elif color == "green":
        return color
    else:
        print("Invalid input")
        quit()
        
def move_pen():
    x_val = get_number("x axis position?> ")
    y_val = get_number("y axis position?> ")
    fred.penup()
    fred.goto(x_val,y_val)
    fred.pendown()
    
# setup window
screen = 500
window = turtle.Screen()
window.screensize(screen,screen)

# create instance of turtle
fred = turtle.Turtle()
fred.shape("turtle")

# get user input
num_sides = get_number("How many sides?> ")
size = get_number("How long are the sides?> ")
fill = get_color()

move_pen()
draw_poly(size,num_sides, fill)