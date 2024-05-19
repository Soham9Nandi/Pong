from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")

screen.tracer(0)

rpaddle = Paddle((350,0))
lpaddle = Paddle((-350,0))
ball = Ball()
scoreboard = Score()

screen.listen()
screen.onkey(rpaddle.go_up, "Up")
screen.onkey(rpaddle.go_down, "Down")

screen.onkey(lpaddle.go_up, "w")
screen.onkey(lpaddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce()

    if ball.distance(rpaddle)<50 and ball.xcor()>320 or ball.distance(lpaddle)<50 and ball.xcor()<-320:
        ball.collision()

    #left wins
    if ball.xcor()>390:
        ball.reset_pos()
        scoreboard.increase_score_left()
    #right wins
    if ball.xcor()<-390:    
        ball.reset_pos()
        scoreboard.increase_score_right()

    if scoreboard.left_score == 10 or scoreboard.right_score == 10:
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()