
from turtle import Turtle
from turtle import Screen
import time
import random

# screen
screen = Screen()
screen.bgcolor("black")
screen.setup(600, 600)
screen.tracer(0)

# score
yellow = 0
purple = 0
screen.title(f"Score:    Yellow: {yellow}   Purple  {purple}")

# game over writting
game_over = Turtle ("circle")
game_over.color("white")
game_over.hideturtle()
game_over.penup()
wait_time = 0.15

# snake 1
head = Turtle("square")
head.color("purple1")
head.penup()
head.goto(+20, 0)
head.direction = "stop"
tail = []

# snake 2
head2 = Turtle("square")
head2.color("gold")
head2.penup()
head2.goto(-20, 0)
head2.direction = "stop"
tail2 = []

# apple
apple = Turtle("circle")
apple.color("green")
apple.penup()

def new_apple():
    numers_x = range (-260, 260, 20)
    numers_y = range(-260, 260, 20)
    apple_x = random.choice(numers_x)
    apple_y = random.choice(numers_y)
    apple.goto(apple_x, apple_y)
    while apple.distance(head) < 20 or apple.distance(head2) < 20:
        new_apple() 
    if len(tail)>0:
        for index in tail:
            if index.distance(apple) < 20:
                new_apple()
    if len(tail2)>0:
        for index in tail2:
            if index.distance(apple) < 20:
                new_apple()

new_apple()

# move function 
def move(he):
    if he.direction == "up":
        y = he.ycor()
        he.sety(y+20)

    if he.direction == "down":
        y = he.ycor()
        he.sety(y-20)

    if he.direction == "right":
        x = he.xcor()
        he.setx(x+20)

    if he.direction == "left":
        x = he.xcor()
        he.setx(x-20)

# response to keys - snake 1
def move_up():
    if head.direction != "down" or len(tail)<1:
        head.direction = "up"
def move_down():
    if head.direction != "up" or len(tail)<1:
        head.direction = "down"
def move_right():
    if head.direction != "left" or len(tail)<1:
        head.direction = "right"
def move_left():
    if head.direction != "right" or len(tail)<1:
        head.direction = "left"

# response to keys - snake 2
def move_u():
    if head2.direction != "down" or len(tail2)<1:
        head2.direction = "up"
def move_d():
    if head2.direction != "up" or len(tail2)<1:
        head2.direction = "down"
def move_r():
    if head2.direction != "left" or len(tail2)<1:
        head2.direction = "right"
def move_l():
    if head2.direction != "right" or len(tail2)<1:
        head2.direction = "left"


screen.listen()

# key setting - snake 1   
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_down, "Down")
screen.onkeypress(move_right, "Right")
screen.onkeypress(move_left, "Left")

#key setting - snake 2
screen.onkeypress(move_u, "w")
screen.onkeypress(move_d, "s")
screen.onkeypress(move_r, "d")
screen.onkeypress(move_l, "a")

# crash and restart the game
def crash():
    game_over.goto(-150,-25)            
    game_over.write("Game over", font=("Ariel", 50))
    head.direction = "stop"
    head2.direction = "stop"

    screen.update()
    time.sleep(3)
    for a in tail:
        a.goto(1000, 1000)
    for a in tail2:
        a.goto(1000, 1000)

    tail.clear()
    tail2.clear()
    game_over.clear()
    head.goto(+20, 0)
    head2.goto(-20, 0)

# game logic
while True:
    screen.title(f"***      Score:    Yellow: {yellow}  /  Purple: {purple}      ***")    
    time.sleep(wait_time)
    move(head)
    move(head2)

    # heads collision
    if head.distance(head2) < 20 or head2.distance(head) < 20:
       crash() 

    # head-tail collision
    for index in tail:
        if index.distance(head) < 20:
            crash()
            purple = 0
                
    for index in tail2: 
        if index.distance(head) < 20:
            crash()
            purple = 0

    for index in tail2:
        if index.distance(head2) < 20:
            crash()
            yellow = 0

    for index in tail:
        if index.distance(head2) < 20:
            crash()
            yellow = 0

    screen.update()
      
    # apple eating
    if head.distance(apple) < 20:
        new_apple()
        new_tail = Turtle("square")
        new_tail.speed(0)
        new_tail.color("Purple4")
        new_tail.penup()
        tail.append(new_tail)
        wait_time -= 0.002
        purple += 1

    if head2.distance(apple) < 20:
        new_apple()
        new_tail2 = Turtle("square")
        new_tail2.speed(0)
        new_tail2.color("gold3")
        new_tail2.penup()
        tail2.append(new_tail2)
        wait_time -= 0.002
        yellow += 1

    # tail growing
    for index in range(len(tail)-1, 0, -1):
        x = tail[index-1].xcor()
        y = tail[index-1].ycor()
        tail[index].goto(x, y)

    for index in range(len(tail2)-1, 0, -1):
        x = tail2[index-1].xcor()
        y = tail2[index-1].ycor()
        tail2[index].goto(x, y)

    
    if len(tail) > 0:
        tail_x = head.xcor()
        tail_y = head.ycor()
        tail[0].goto(tail_x,tail_y)

    if len(tail2) > 0:
        tail2_x = head2.xcor()
        tail2_y = head2.ycor()
        tail2[0].goto(tail2_x, tail2_y)
    
    # go trough the screen
    if head.xcor() < -280:
        y = head.ycor()
        head.goto(+280, y)
    if head.xcor() > 280:
        y = head.ycor()
        head.goto(-280, y)
    if head.ycor() < -280:
        x = head.xcor()
        head.goto(x, 280)
    if head.ycor() > 280:
        x = head.xcor()
        head.goto(x, -280)

    if head2.xcor() < -280:
        y = head2.ycor()
        head2.goto(+280, y)
    if head2.xcor() > 280:
        y = head2.ycor()
        head2.goto(-280, y)
    if head2.ycor() < -280:
        x = head2.xcor()
        head2.goto(x, 280)
    if head2.ycor() > 280:
        x = head2.xcor()
        head2.goto(x, -280)
            
        


screen.exitonclick()