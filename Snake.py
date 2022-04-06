import turtle as tr
import time as t
import random as r

delay = 0.1
score = high_score = 0

window = tr.Screen()
window.title("Snake Game")
window.bgcolor("black")
window.setup(width=600, height=600)
window.tracer(0)

#head
head = tr.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

#food
food = tr.Turtle()
colors = r.choice(['green', 'blue', 'red'])
shapes = r.choice(['circle', 'square', 'triangle'])
food.color(colors)
food.shape(shapes)
food.speed(0)
food.penup()
food.goto(0, 100)

#pen
pen = tr.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score: 0     High Score: 0", align="center", font=("consolas", 20, "bold"))

def goUp():
    if head.direction != "down":
        head.direction = "up"

def goDown():
    if head.direction != "up":
        head.direction = "down"

def goLeft():
    if head.direction != "right":
        head.direction = "left"

def goRight():
    if head.direction != "left":
        head.direction = "right"

def Move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    elif head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    elif head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    elif head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

def Stop():
    tr.bye()

def Play():
    global score, high_score, delay
    window.update()
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        t.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        colors = r.choice(['green', 'red', 'blue'])
        shapes = r.choice(['square', 'circle'])
        for i in seg:
            i.goto(1000, 1000)
        seg.clear()
        score, delay = 0, 0.1
        pen.clear()
        pen.write("Score: {}    High Score: {}".format(score, high_score), align="center", font=("consolas", 20, "bold"))
    if head.distance(food) < 20:
        x, y = r.randint(-270, 270), r.randint(-270, 270)
        food.goto(x, y)
        new_seg = tr.Turtle()
        new_seg.speed(0)
        new_seg.shape("square")
        new_seg.color("orange")
        new_seg.penup()
        seg.append(new_seg)
        delay -= 0.001
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {}    High Score: {}".format(score, high_score), align="center", font=("consolas", 20, "bold"))
    for i in range(len(seg) - 1, 0, -1):
        x, y = seg[i - 1].xcor(), seg[i - 1].ycor()
        seg[i].goto(x, y)
    if len(seg) > 0:
        x, y = head.xcor(), head.ycor()
        seg[0].goto(x, y)
    Move()
    for i in seg:
        if i.distance(head) < 20:
            t.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            colors = r.choice(['green', 'red', 'blue'])
            shapes = r.choice(['square', 'circle'])
            for i in seg:
                i.goto(1000, 1000)
            seg.clear()
            score, delay = 0, 0.1
            pen.clear()
            pen.write("Score: {}    High Score: {}".format(score, high_score), align="center", font=("consolas", 20, "bold"))
    t.sleep(delay)

if __name__ == "__main__":
    window.listen()
    window.onkeypress(goUp, "Up")
    window.onkeypress(goDown, "Down")
    window.onkeypress(goLeft, "Left")
    window.onkeypress(goRight, "Right")
    window.onkeypress(Stop, 'Escape')
    seg = []
    while True:
        Play()
    window.mainloop()
