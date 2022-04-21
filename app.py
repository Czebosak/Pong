# Basic setup
import turtle
import winsound

wn = turtle.Screen()
wn.title("Epic Pong!!1!!1!!!11")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Variables
player_1_score = 0
player_2_score = 0

# Paddle 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350, 0)

# Paddle 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Player 1: {player_1_score}  Player 2: {player_2_score}", align="center", font=("Courier", 24, "normal"))

# Functions
def paddle_1_up():
    y = paddle_1.ycor()
    paddle_1.sety(y + 20)

def paddle_1_down():
    y = paddle_1.ycor()
    paddle_1.sety(y - 20)

def paddle_2_up():
    y = paddle_2.ycor()
    paddle_2.sety(y + 20)

def paddle_2_down():
    y = paddle_2.ycor()
    paddle_2.sety(y - 20)

# Keybinds
wn.listen()
wn.onkeypress(paddle_1_up, "w")
wn.onkeypress(paddle_1_down, "s")
wn.onkeypress(paddle_2_up, "Up")
wn.onkeypress(paddle_2_down, "Down")


# Main game loop
while True:
    wn.update()

    # Ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Ball Bounce
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("wall.wav", winsound.SND_ASYNC)

    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("wall.wav", winsound.SND_ASYNC)

    
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx = -0.1
        ball.dy = -0.1
        player_1_score += 1
        pen.clear()
        pen.write(f"Player 1: {player_1_score}  Player 2: {player_2_score}", align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("score.wav", winsound.SND_ASYNC)
    
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        ball.dx = 0.1
        ball.dy = 0.1
        player_2_score += 1
        pen.clear()
        pen.write(f"Player 1: {player_1_score}  Player 2: {player_2_score}", align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("score.wav", winsound.SND_ASYNC)

    # Collisions
    if ball.xcor() > paddle_2.xcor() - 10 and ball.xcor() < paddle_2.xcor() + 10 and (ball.ycor() < paddle_2.ycor() + 50 and ball.ycor() > paddle_2.ycor() - 50):
        ball.setx(paddle_2.xcor() - 10)
        ball.dx *= -1.1
        winsound.PlaySound("paddle.wav", winsound.SND_ASYNC)
    
    if ball.xcor() > paddle_1.xcor() - 10 and ball.xcor() < paddle_1.xcor() + 10 and (ball.ycor() < paddle_1.ycor() + 50 and ball.ycor() > paddle_1.ycor() - 50):
        ball.setx(paddle_1.xcor() + 10)
        ball.dx *= -1.05
        winsound.PlaySound("paddle.wav", winsound.SND_ASYNC)