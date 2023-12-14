# Turtle-race-using-python
## 1.Importing Libraries:

from turtle import Turtle, Screen
import random
Here, the script imports the Turtle class and the Screen class from the Turtle graphics library, as well as the random module.

## 2.Setting up the Screen:
screen = Screen()
screen.setup(width=500, height=400)
This creates a Turtle graphics window with a width of 500 pixels and a height of 400 pixels.

## 3.Initializing Variables:
isRaceon = False
The variable isRaceon is set to False initially.

## 4.User Input Function:
def userin():
    return screen.textinput(title="Place your bet", prompt="Choose your turtle color")
This function prompts the user to input their bet on a turtle color.

## 5.Turtle Setup:
renColor = ["red", "blue", "yellow", "orange", "purple", "green"]
Yaxis = [-70, -40, -10, 20, 50, 80]
allTurtle = []

for i in range(6):
    aji = Turtle(shape="turtle")
    aji.color(renColor[i])
    aji.penup()
    aji.goto(x=-230, y=Yaxis[i])
    allTurtle.append(aji)
This sets up six turtles with different colors and positions them on the starting line.

## 6.User Bets on a Turtle:
userBet = userin()

while userBet not in renColor:
    userBet = userin()
The user is prompted to choose a turtle color for betting. The loop ensures that the user's input is a valid color.

## 7.Turtle Race Loop:
isRaceon = True

while isRaceon:
    for turtles in allTurtle:
        if turtles.xcor() > 230:
            isRaceon = False
            winColor = turtles.pencolor()
            if winColor == userBet:
                print(f"Yours {winColor} is the winner!")
                screen.textinput(title="Race Result", prompt=f"Yours {winColor} is the winner!")
            else:
                print(f"You lost. {winColor} is the winner.")
                screen.textinput(title="Race Result", prompt=f"You lost. {winColor} is the winner.")
        rand_distance = random.randint(0, 10)
        turtles.forward(rand_distance)

screen.exitonclick()

## Output:
https://app.screencast.com/proONfWYih76a

## Conclusion
The main race loop moves each turtle forward by a random distance in each iteration. If a turtle reaches the finish line (x-coordinate > 230), the race ends. The program then checks if the winning turtle's color matches the user's bet and displays the result.

Finally, the Turtle graphics window exits when clicked.

This script essentially simulates a turtle race where the user can bet on one of the turtles, and the race outcome is determined randomly. The result is displayed both in the console and in a pop-up window.
