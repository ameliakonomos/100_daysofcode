from turtle import Turtle, Screen
import random
import turtle as t

tim = t.Turtle()
t.colormode(255)
# colors = ["DarkOrchid", "IndianRed", "DeepSkyBlue"]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

#random walk is used in math and physics
#can model real life situations
directions = [0, 90, 180, 270] #north east south west
tim.pensize(15)
tim.speed("fastest")

for i in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))



screen = Screen() #import
screen.exitonclick() #window will not dissapear