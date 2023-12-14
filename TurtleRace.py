from turtle import Turtle, Screen
import random
screen=Screen()
screen.setup(width=500, height=400)
isRaceon=False
def userin():
    return screen.textinput(title="place your bet", prompt="Choose your turtle colour")

renColor=["red","blue","yellow","orange","purple","green"]
Yaxis=[-70,-40,-10,20,50,80]
allTurtle=[]
for i in range(0,6):
    aji = Turtle(shape="turtle")
    aji.color(renColor[i])
    aji.penup()
    aji.goto(x=-230, y=Yaxis[i])
    allTurtle.append(aji)
userBet=userin()

while userBet not in renColor:
    userBet = userin()
isRaceon=True
while  isRaceon:
    for turtles in allTurtle:
        if turtles.xcor()>230:
            isRaceon=False
            winColor=turtles.pencolor()
            if winColor==userBet:
                print(f"yours {winColor} is win")
                screen.textinput(title="Race Result", prompt=f"yours {winColor} is win")
            else:
                print(f"you loss {winColor} is win")
                screen.textinput(title="Race Result", prompt=f"you loss {winColor} is win")
        rand_distance=random.randint(0,10)
        turtles.forward(rand_distance)


screen.exitonclick()
