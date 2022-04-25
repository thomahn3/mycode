import turtle

def draw_poly(length, sides):
    for i in range(sides):
        fred.forward(length)
        fred.right(360/sides)
        
# setup window
screen = 500
window = turtle.Screen()
window.setup(screen,screen)

# create instance of turtle
fred = turtle.Turtle()
fred.shape("turtle")

sides = int(input("How many sides? ->"))
length = int(input("How long are the sides? ->"))

draw_poly(length,sides)