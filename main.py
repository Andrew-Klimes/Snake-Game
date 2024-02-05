from turtle import Turtle, Screen
import time
import random

screen = Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.title("SNAKE GAME")
screen.tracer(False)

# Atributy Skóre 
score = 0
highest_score = 0

# Hadí hlava + jablka + score
head = Turtle("square")
head.color("black")
head.speed(0)
head.penup()
head.goto(0, 0)
head.direction = "stop"

apple = Turtle("circle")
apple.color("red")
apple.penup()
apple.goto(100, 100)

score_text = Turtle()
score_text.color("black")
score_text.speed(0)
score_text.penup()
score_text.hideturtle()
score_text.goto(0, 260)
score_text.write("Skóre: 0   Nejvyšší scóre: 0", align= "center", font=("Arial", 18))

# Tělo hada
body_parts = []

# Pomocné Funkce
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
        
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
        
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

def move_up():
    if head.direction != "down":
        head.direction = "up"

def move_down():
    if head.direction != "up":
        head.direction = "down"

def move_right():
    if head.direction != "left":
        head.direction = "right"

def move_left():
    if head.direction != "right":
        head.direction = "left"

# funkce na resetování skóre
def reset():
    score_text.clear()
    score_text.write(f"Skóre: {score}   Nejvyšší scóre: {highest_score}", align= "center", font=("Arial", 18))
    
# Pohyb klávesnicí
screen.listen()
screen.onkeypress(move_up, "w")
screen.onkeypress(move_down, "s")
screen.onkeypress(move_right, "d")
screen.onkeypress(move_left, "a")

# Hlavní cyklus
while True:
    screen.update()
    
    # Srážka hlavy s okrajem obrazovky
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(2)
        head.goto(0, 0)
        head.direction = "stop"
        
        # Skryjeme části těla
        for one_body_part in body_parts:
            one_body_part.goto(1500, 1500)
            
        # Vyčištění listu s částmi těla po srážce
        body_parts.clear()
        
        # Nulování scóre po srážce
        score = 0
        reset()
    
    # Had požírá jablko
    if head.distance(apple) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        apple.goto(x, y)
        
        # tělo hada
        body_part = Turtle("square")
        body_part.color("grey")
        body_part.speed(0)
        body_part.penup()
        body_parts.append(body_part)
        
        # Připisování Skóre
        score += 10
        if score > highest_score:
            highest_score = score
            
        score_text.clear()
        score_text.write(f"Skóre: {score}   Nejvyšší scóre: {highest_score}", align= "center", font=("Arial", 18))
    
    # Přidávání části těla hada
    for index in range(len(body_parts)-1, 0, -1):
        x = body_parts[index - 1].xcor()
        y = body_parts[index - 1].ycor()
        body_parts[index].goto(x, y)
        
    if len(body_parts) > 0:
        x = head.xcor()
        y = head.ycor()
        body_parts[0].goto(x, y)
        
    move()
    
    # Srážka hlavy s tělem hada
    
    for one_body_part in body_parts:
        if one_body_part.distance(head) < 20:
            time.sleep(2)
            head.goto(0, 0)
            head.direction = "stop"
        
            # Skryjeme části těla
            for one_body_part in body_parts:
                one_body_part.goto(1500, 1500)
                
            # Vyčištění listu s částmi těla po srážce
            body_parts.clear()
            
            # Nulování scóre po srážce
            score = 0
            reset()

    time.sleep(0.1)

screen.exitonclick()
