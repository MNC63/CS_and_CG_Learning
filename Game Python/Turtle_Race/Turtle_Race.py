from turtle import Turtle, Screen
from random import randint

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
STARTING_X = -380
FINISH_LINE = 370
STARTING_Y = -300
DISTANCE_BETWEEN_TURTLES = 75
#Def the variables

Start_race = False
display = Screen()
display.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
# set the screen size

user_choice = display.textinput(title= "Enter your bet: ", prompt ="red, blue, green,...")
# get the user input for the color of the turtle

if user_choice:
    Start_Race = True
# check if the user has entered a color
turtle_list = []
distance = 0
colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink"]
# create a list of colors

for i in range(7):
    Race = Turtle(shape = "turtle")
    Race.color(colors[i])
    Race.penup()
    distance += DISTANCE_BETWEEN_TURTLES
    Race.goto(STARTING_X, STARTING_Y + distance)
    turtle_list.append(Race)
# for loop to create turtles and set their colors and positions

result_turtle = Turtle()
result_turtle.hideturtle()
result_turtle.penup()
result_turtle.goto(0, 0)
#ceate a turtle to display the result message




while Start_Race:
    for turtle_each in turtle_list:
        if turtle_each.xcor() > FINISH_LINE:
            Start_Race = False
            wining_clor = turtle_each.pencolor()
            if wining_clor == user_choice:
                result_turtle.write("You Win!", align = "center", font = ("Arial", 30, "bold"))
            else:
                result_turtle.write(f"You Lose! {wining_clor.title()} won.", align = "center", font = ("Arial", 30, "bold"))
            break #exit the loop after finishing the race
        turtle_each.forward(randint(1, 10))
#while loop to move the turtles forward by a random distance

display.exitonclick()