import turtle as t
import random as r
def right():
    player.forward(10)
def left():
    player.forward(-10)    
t.bgcolor("lightpink")
t.setup(500, 700)
ball = t.Turtle()
ball.shape("circle")
player = t.Turtle()
player.shape("square")
player.shapesize(1, 5)
player.up()
player.speed(0)
player.goto(0, -270)
t.listen()
t.onkeypress(right, "Right")
t.onkeypress(left, "Left")
while True:
    ball.forward(10)
    print(ball.xcor())
    if ball.xcor() >= 250:
        ball.right(r.randint(10,90))
    if ball.xcor() <= -250:
        ball.right(r.randint(10,90))
    if ball.ycor() >= 350:
        ball.right(r.randint(10,90))    
    if ball.ycor() <= -350:
        ball.right(r.randint(10,90))
t.mainloop()
