import turtle

def draw_poly(length, sides, color):
    fred.color("black", color)
    fred.begin_fill()
    for i in range(sides):
        fred.forward(length)
        fred.right(360/sides)
    fred.end_fill()
        
def get_number(prompt):
    num = input(prompt)
    if num.isdigit():
        return int(num)
    else:
        print("Invalid input")
        quit()
        
def get_color():
    color = input("Fill colour (red, blue, green)?> ").lower()
    if color == "red":
        return color
    elif color == "blue":
        return color
    elif color == "green":
        return color
    else:
        print("Invalid  input")
        quit()
        
# setup window
screen = 500
window = turtle.Screen()
window.setup(screen,screen)

# create instance of turtle
fred = turtle.Turtle()
fred.shape("turtle")

# get user input
sides = get_number("How many sides?> ")
length = get_number("How long are the sides?> ")
fill = get_color()

draw_poly(length,sides,fill)