import turtle


turtle.setup(750, 600)
turtle.bgcolor("purple")

paddle1 = turtle.Turtle()
paddle1.shape("square")
paddle1.color("white")
paddle1.shapesize(stretch_wid=5, stretch_len=1) 
paddle1.penup()
paddle1.goto(-350, 0)
paddle1.dy = 0

paddle2 = turtle.Turtle()
paddle2.shape("square")
paddle2.color("orange")
paddle2.shapesize(stretch_wid=5, stretch_len=1)
paddle2.penup()
paddle2.goto(350, 0)
paddle2.dy = 0

ball = turtle.Turtle()
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(0, 0)
ball.dx = 6
ball.dy = -6

game_over = False
winner = None
points = {
    "player1": 0,
    "player2": 0
}
game_rules = {
    "max_points": 5,
}


score_display = turtle.Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("P1: 0  P2: 0", align="center", font=("Arial", 24, "normal"))


def paddle1_up():
    y = paddle1.ycor()
    y += 10
    paddle1.sety(y)

def paddle1_down():
    y = paddle1.ycor()
    y -= 10
    paddle1.sety(y)

def paddle2_up():
    y = paddle2.ycor()
    y += 10
    paddle2.sety(y)


def paddle2_down():
    y2 = paddle2.ycor()
    y2 -= 10
    paddle2.sety(y2)

"""

more fun version is where the paddles are continously updated, players have to be more focused
code below. reminder on what to replace in the paddle controls
"""
    #paddle2.dy = -10

turtle.listen()
turtle.onkeypress(paddle1_up, "s")
turtle.onkeypress(paddle1_down, "x")
turtle.onkeypress(paddle2_up, "Up")
turtle.onkeypress(paddle2_down,"Down")






while True:
    
    turtle.update()
   


    paddle1.sety(paddle1.ycor() + paddle1.dy)
    paddle2.sety(paddle2.ycor() + paddle2.dy)



    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Check for game over conditions
    if points["player1"] == game_rules["max_points"]:
        game_over = True
        winner = "P1"
    elif points["player2"] == game_rules["max_points"]:
        game_over = True
        winner = "P2"

    #ball collision, paddles
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle2.ycor() + 60 and ball.ycor() > paddle2.ycor() - 60):
        ball.setx(340)
        ball.dx *= -1
    elif (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle1.ycor() + 60 and ball.ycor() > paddle1.ycor() - 60):
        ball.setx(-340)
        ball.dx *= -1

    # ball hitting behind paddles for point
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        points["player1"] += 1
        score_display.clear()
    elif ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        points["player2"] += 1
        score_display.clear()

    # ball hitting top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1


    
    score_display.write("P1: {}  P2: {}".format(points["player1"], points["player2"]), align="center", font=("Arial", 24, "normal"))

    if game_over == True:
        game_over_display = turtle.Turtle()
        game_over_display.color("white")
        game_over_display.penup()
        game_over_display.hideturtle()
        game_over_display.goto(0, 0)
        game_over_display.write("WE HAVE A WINNER! \n{} Is The Pong Champion!".format(winner), align="center", font=("Arial", 40, "normal"))

    
    