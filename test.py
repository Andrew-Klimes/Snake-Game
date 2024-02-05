from turtle import Turtle, Screen
import time
import random

# Nastavení obrazovky
screen = Screen()
screen.bgcolor("green")
screen.screensize(400, 400)
screen.title("SNAKE GAME")


# Hadí hlava
head = Turtle("square")
head.color("black")
head.goto(0, 0)
head.speed(0)
head.penup()
head.move = "up"

# Pohyb hlavy

def move():
    if head.move == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.move == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.move == "right":
        x = head.xcor()
        head.setx(x + 20)
        
    if head.move == "left":
        x = head.xcor()
        head.setx(x - 20)

def move_up():
    if head.move != "down":
        head.move = "up"
    
def move_down():
    if head.move != "up":
        head.move = "down"

def move_right():
    if head.move != "left":
        head.move = "right"

def move_left():
    if head.move != "right":
        head.move = "left"

# pohyb pomocí klávesnice
screen.listen()
screen.onkeypress(move_up, "w")
screen.onkeypress(move_down, "s")
screen.onkeypress(move_right, "d")
screen.onkeypress(move_left, "a")

while True:

    move()
    
    time.sleep(0.1)

screen.exitonclick()
