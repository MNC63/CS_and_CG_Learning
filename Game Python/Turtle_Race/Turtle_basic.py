from turtle import Turtle, Screen

T = Turtle()
# create a turtle object
T.color("green")
T.shape("turtle")


def Forward():
    T.forward(10)
def Backward():
    T.backward(10)
def Left():
    Angle = T.heading()
    T.setheading(Angle + 10)
def Right():
    Angle = T.heading()
    T.setheading(Angle - 10)
    

display = Screen()
display.listen()

display.onkey(key = "Up", fun = Forward)
display.onkey(key = "Down", fun = Backward)
display.onkey(key = "Left", fun = Left)
display.onkey(key = "Right", fun = Right)

display.exitonclick()



















# set the color and shape of the turtle
#me.forward(200)
# move the turtle forward by 400 units
#me.right(90)
# turn the turtle right by 90 degrees
#me.forward(200)

# for i in range(4):
#     me.forward(200)
#     me.right(90)
# draw a square

# for _ in range(4):
#     for _ in range(10):
#         me.forward(7)
#         me.penup()
#         me.forward(10)
#         me.pendown()
#     me.right(90)
# # draw a square with a gap of 10 units between each line








