#AUTHOR: DAN ODIN
#DATE: 04-2023

import os
from turtle import Turtle, Screen, Shape
from random import randint

screen = Screen()
screen.setup(750, 600)
screen.tracer(0)
screen.bgcolor("gray")
screen.title("Pong Classic")

"""
FRAME RATE

Frame rate is collected because the flow of the game is controlled by setting screen.tracer(0) 
which in turn lets the code control how much frames are rendered for smoother play instead of using a while loop,
as you know.. while loops aren't good for something like this
"""

frame_rate = 42

"""
PLAYER NAMES

player1 and player2 as p1-p2, is an input variable for taking for taking first player and second player names,
after the names are inserted the game starts

where the names are used the number of string required are 3 from the inputted name, so {p1[2]}, {p2[2]} is used

"""
p1 = str(input("First Player > ")).upper()
p2 = str(input("Second Player > ")).upper()


"""
GAME RULES

This sets the rules for the games, at the moment this will know when the game is over and who to give the win

"""

game_over = False
winner = None
points = {
    "player1": 0,
    "player2": 0
}
game_rules = {
    "max_points": 10,
}

"""
PLAY ZONE

The black playable area on the screen

"""

play_area_top = screen.window_height() / 2 - 150  # top of play subtracted by 100
play_area_bottom = -screen.window_height() / 2 + 150  # 100 from bottom
play_area_left = -screen.window_width() / 2 + 120  # 50 from left
play_area_right = screen.window_width() / 2 - 120  # 50 from right

area = Turtle()
area.hideturtle()
area.penup()
area.color("black")
area.begin_fill()
area.goto(play_area_right, play_area_top)
area.pendown()

area.goto(play_area_left, play_area_top)
area.goto(play_area_left, play_area_bottom)

area.goto(play_area_right, play_area_bottom)

area.goto(play_area_right, play_area_top)
area.end_fill()

# PADDLES

L = Turtle()
R = Turtle()
L.penup()
R.penup()

# Paddles shape
paddle_w_half = 10 / 2  # 10 units wide
paddle_h_half = 40 / 2  # 40 units high
paddle_shape = Shape("compound")
paddle_points = ((-paddle_h_half, -paddle_w_half),
                 (-paddle_h_half, paddle_w_half),
                 (paddle_h_half, paddle_w_half),
                 (paddle_h_half, -paddle_w_half))
paddle_shape.addcomponent(paddle_points, "orange",)
screen.register_shape("paddle", paddle_shape)
L.shape("paddle")
L.color("green")
R.shape("paddle")
R.color("orange")

# Spawn paddles into corners
L.setx(play_area_left + 10)
R.setx(play_area_right - 10)

paddle_L_move_direction = 0  # L paddle movement direction in next frame
paddle_R_move_direction = 0  # R paddle movement direction in next frame

paddle_move_vert = 10  # Vertical movement distance per frame


def paddle_is_allowed_to_move_here(new_y_pos):
    if play_area_bottom > new_y_pos - paddle_h_half:  # bottom of paddle below bottom of field
        return False
    if new_y_pos + paddle_h_half > play_area_top:  # top of paddle above top of field
        return False
    return True


def update_paddle_positions():
    l_new_y_pos = L.ycor() + (paddle_L_move_direction * paddle_move_vert)
    r_new_y_pos = R.ycor() + (paddle_R_move_direction * paddle_move_vert)
    if paddle_is_allowed_to_move_here(l_new_y_pos):
        L.sety(l_new_y_pos)
    if paddle_is_allowed_to_move_here(r_new_y_pos):
        R.sety(r_new_y_pos)


def l_up():
    global paddle_L_move_direction
    paddle_L_move_direction = 1


def l_down():
    global paddle_L_move_direction
    paddle_L_move_direction = -1


def l_off():
    global paddle_L_move_direction
    paddle_L_move_direction = 0


def r_up():
    global paddle_R_move_direction
    paddle_R_move_direction = 1


def r_down():
    global paddle_R_move_direction
    paddle_R_move_direction = -1


def r_off():
    global paddle_R_move_direction
    paddle_R_move_direction = 0

def restart():
    global score_L, score_R
    score_L, score_R = 0, 0
    frame_rate = 42


screen.onkeypress(l_up, "w")
screen.onkeypress(l_down, "z")
screen.onkeypress(r_up, "Up")
screen.onkeypress(r_down, "Down")
screen.onkeyrelease(l_off, "w")
screen.onkeyrelease(l_off, "z")
screen.onkey(restart, "R")
screen.onkeyrelease(r_off, "Up")
screen.onkeyrelease(r_off, "Down")
screen.listen()

# SCORE

score_turtle = Turtle()
score_turtle.penup()
score_turtle.hideturtle()

score_L = 0
score_R = 0

game_title = Turtle()
game_title.penup()
game_title.hideturtle()


def add_game_title():
    game_title.clear()
    game_title.goto(-screen.window_width() / 110, screen.window_height() / 2 - 80)
    game_title.write("PONG CLASSIC", align="center", font=("Verdana", 42, "bold"))
    game_title.goto(-screen.window_width() / 110, screen.window_height() / 2 - 99)
    game_title.write("(DanDaPanda.games)", align="center", font=("Arial", 10, "normal"))


def update_scores():
    score_turtle.clear()
    score_turtle.goto(-screen.window_width() / 8, screen.window_height() / 2 - 550)
    score_turtle.write(f'{p1[0]}{p1[1]}{p1[2]} {score_L}', align="center", font=("Verdana", 32, "bold"))

    score_turtle.goto(-screen.window_width() / 112, screen.window_height() / 2 - 550)

    score_turtle.write(" :", align="center", font=("Verdana", 32, "bold"))

    score_turtle.goto(screen.window_width() / 112, screen.window_height() / 2 - 550)

    score_turtle.goto(screen.window_width() / 8, screen.window_height() / 2 - 550)
    score_turtle.write(f'{score_R} {p2[0]}{p2[1]}{p2[2]}', align="center", font=("Verdana", 32, "bold"))


def check_scores():
    global score_L, score_R
    if (ball.xcor() + ball_radius) >= play_area_right:  # right of ball at right of field

        score_L += 1
        points["player1"] += score_L
        os.system("aplay cheer2.wav&")
        update_scores()
        reset_ball()
    elif play_area_left >= (ball.xcor() - ball_radius):  # left of ball at left of field
        score_R += 1
        points["player2"] += score_R
        os.system("aplay cheer1.wav&")
        update_scores()
        reset_ball()


# BALL

ball = Turtle()
ball.penup()
ball.shape("circle")  # Use the built-in shape "circle"
ball.color("white")
ball.shapesize(0.5, 0.5)  # Stretch it to half default size
ball_radius = 10 * 0.5  # Save the new radius for later

ball_move_horizontally = 3  # Horizontal movement per frame
ball_move_vertically = 5  # Vertical movement per frame


def ball_collides_with_paddle(paddle):
    x_distance = abs(paddle.xcor() - ball.xcor())

    y_distance = abs(paddle.ycor() - ball.ycor())

    overlap_horizontally = (ball_radius + paddle_w_half >= x_distance)  # either True or False
    overlap_vertically = (ball_radius + paddle_h_half >= y_distance)  # either True or False

    if overlap_horizontally and overlap_vertically is True:
        os.system("aplay bounce.wav&")

    return overlap_horizontally and overlap_vertically  # so it returns either True or False


def update_ball_position():
    global ball_move_horizontally, ball_move_vertically
    if ball.ycor() + ball_radius >= play_area_top:  # top of ball at or above top of field
        os.system("aplay bounce_wall.wav&")
        ball_move_vertically *= -1
    elif play_area_bottom >= ball.ycor() - ball_radius:  # bottom of ball at or below bottom of field
        os.system("aplay bounce_wall.wav&")
        ball_move_vertically *= -1
    if ball_collides_with_paddle(R) or ball_collides_with_paddle(L):
        ball_move_horizontally *= -1
    ball.setx(ball.xcor() + ball_move_horizontally)
    ball.sety(ball.ycor() + ball_move_vertically)



def reset_ball():
    global ball_move_vertically, ball_move_horizontally
    ball.setpos(0, 0)
    horizontal_speed = randint(5, 10)
    speed_vert = randint(5, 10)
    horizontal_direction = 1
    vertical_direction = 1
    if randint(0, 100) > 50:  # 50% chance of going left instead of right
        horizontal_direction = -1
    if randint(0, 100) > 50:  # 50% chance of going down instead of up
        vertical_direction = -1
    ball_move_horizontally = horizontal_direction * horizontal_speed
    ball_move_vertically = vertical_direction * speed_vert


# FRAME


# GAME OVER
def game_over_checker():
    global game_over, winner, frame_rate
    if score_L == 10:
        game_over = True
        winner = f'{p1[0]}{p1[1]}{p1[2]}'
    elif score_R == 10:
        game_over = True
        winner = f'{p2[0]}{p2[1]}{p2[2]}'

    if game_over:
        frame_rate = 100000
        game_over_display = Turtle()
        game_over_display.color("white")
        game_over_display.penup()
        game_over_display.hideturtle()
        game_over_display.goto(0, 0)
        game_over_display.write(f"WE HAVE A WINNER! \n\n\n{winner} IS THE PONG CHAMPION! \n\n Click on 'R' key to restart the game.", align="center",
                                font=("Arial", 20, "bold"))

"""
Game is able to run with this function
"""
def physics_process():

    check_scores()
    update_paddle_positions()
    update_ball_position()
    game_over_checker()
    screen.update()  # show the new frame
    screen.ontimer(physics_process, frame_rate)  # schedule this function to be called again a bit later

add_game_title()
update_scores()
physics_process()
screen.mainloop()
screen.onkey(restart, "R")
