from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.left_score = 0
        self.right_score = 0
        self.hideturtle()

        self.goto(-100,200)
        self.write(self.left_score,align='center',font=("Courier",50,"normal"))

        self.goto(100,200)
        self.write(self.right_score,align='center',font=("Courier",50,"normal"))

        self.update_score()
    def update_score(self):
        self.goto(-100,200)
        self.write(self.left_score,align='center',font=("Courier",50,"normal"))

        self.goto(100,200)
        self.write(self.right_score,align='center',font=("Courier",50,"normal"))

    def increase_score_left(self):
        self.left_score +=1
        self.clear()
        self.update_score()
    def increase_score_right(self):
        self.right_score +=1
        self.clear()
        self.update_score()    
    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", align = 'center', font=("Arial", 24, "normal"))