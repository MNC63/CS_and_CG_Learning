from turtle import Turtle, Screen
import random
import time

#create variables for the screen size and starting position of the turtle
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 600
STARTING_X = 0
STARTING_Y = -250
COLORS = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "white"]
y_pos = random.randint(-250, 250)
STARINTG_VEHICLE_X = 260


#creata a class Cross that inherits from the Turtle class
class Cross(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("yellow")
        self.goto(STARTING_X, STARTING_Y)
        self.setheading(90)

class Vehicle(Turtle):
    def __init__(self):
        super().__init__()
        self.vehicle_list = []
    
    def rand_vehicle(self):
        car = Turtle()
        car.shape("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        car.color(random.choice(COLORS))
        car.goto(STARINTG_VEHICLE_X, y_pos)
        self.vehicle_list.append(car)

        

#def move(self,x,y):
    def Up(self):
        y_pos = self.ycor() +10
        self.goto(self.xcor(), y_pos)
    
    def Down(self):
        y_pos= self.ycor() -10
        self.goto(self.xcor(), y_pos)

    def Right(self):
        x_pos = self.xcor() +10
        self.goto(x_pos, self.ycor())
    
    def Left(self):
        x_pos = self.xcor() -10
        self.goto(x_pos, self.ycor())

#create a screen object and set the size and background color
display = Screen()
display.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
display.bgcolor("black")
display.title("Turtle Cross")
display.tracer(0)

#display the turtle on the screen
turtle_cross = Cross()
vehicle_cross = Vehicle()

#create a key blindings for the turtle to move up, down, left and right
display.listen()
display.onkey(turtle_cross.up, "up")
display.onkey(turtle_cross.down, "down")
# display.onkey(turtle_cross.right, "d")
# display.onkey(turtle_cross.left, "a")

Start_cross = True
while Start_cross:
    time.sleep(0.3)
    display.update()
    vehicle_cross.rand_vehicle()


display.exitonclick()
# display.mainloop()

