from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race ? Enter a color")
print(user_bet)
new_turtle = Turtle()
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'pink', 'purple']
y_position = [-150, -100, -50, 0, 50, 100, 150]
is_race_on = False
all_turtles = []

for turtle_index in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            print(turtle.color())
            win_color = turtle.color()
            is_race_on = False

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

if user_bet == win_color:
    print("You win")
else:
    print("You loose")

screen.exitonclick()
