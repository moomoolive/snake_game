from turtle import Turtle
import random
import time

class head(Turtle):
    def __init__(self, color):
        super().__init__(shape='square')
        self.pu()
        self.color(color)
        self.goto(0,0)
        self.seth(90)
        self.speed(0)

    def move_up(self):
        if self.heading() != 270:    
            self.seth(90)

    def move_down(self):
        if self.heading() != 90: 
            self.seth(270)
    
    def move_left(self):
        if self.heading() != 0: 
            self.seth(180)

    def move_right(self):
        if self.heading() != 180: 
            self.seth(0)

    def move(self):
        y = self.ycor()
        x = self.xcor()

        if self.heading() == 90:           
            self.sety(y + 20)

        if self.heading() == 270:
            self.sety(y - 20)

        if self.heading() == 0:
            self.setx(x + 20)

        if self.heading() == 180:
            self.setx(x - 20)

    @staticmethod
    def slow_game_down(seconds):
        time.sleep(seconds)


class food(Turtle):
    def __init__(self):
        super().__init__(shape='circle')
        self.speed(0)
        self.color('red')
        self.pu()
        self.goto(0,100)

    def move_to_random_location(self):
        x = random.randint(-285, 285)
        y = random.randint(-270, 270)
        self.goto(x, y)

class display_text(Turtle):
    def __init__(self, position, what_you_want_to_display, font_size):
        super().__init__(shape='square')
        self.pu()
        self.hideturtle()
        self.goto(position)
        self.display = self.write(what_you_want_to_display, align='center', font=("Courier", font_size, "normal"))

    def refresh_score(self):
        self.clear()
        return self.display

