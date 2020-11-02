import turtle
import winsound
from classes import head, food, display_text

window = turtle.Screen()
window.title("Snake Game by Moomoolive")
window.bgcolor("green")
window.setup(width=600, height=600)
window.tracer(0)

snake_head = head('black')

def main():
    score = 0
    high_score = 0

    window.listen()
    gamecontrols()

    snake_food = food() 
    snake_tail = []

    while True:
        window.update()

        escape_message = display_text((0,-260), "Press 'Esc' to close game", 14)
        score_display = display_text((0,260), "Score: {} High Score: {}".format(score, high_score), 24)

        #border checking
        if snake_head.xcor() > 290 or snake_head.xcor() < -290 or snake_head.ycor() > 290 or snake_head.ycor() < -290:
            reset_score()

            for segment in snake_tail:
                segment.goto(1000, 1000)

            snake_tail.clear()
            score = 0

        #eating food and growing snaketail
        if snake_head.distance(snake_food) < 20:
            snake_food.move_to_random_location()
            winsound.PlaySound("chomp.wav", winsound.SND_ASYNC)

            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("grey")
            new_segment.penup()
            snake_tail.append(new_segment)

            score += 10

            score_display.refresh_score()

            if score > high_score:
                high_score = score
                winsound.PlaySound("high_score.wav", winsound.SND_ASYNC)
        
        #snake tail movement
        for index in range(len(snake_tail)-1, 0, -1):
            x = snake_tail[index-1].xcor()
            y = snake_tail[index-1].ycor()
            snake_tail[index].goto(x, y)

        if len(snake_tail) > 0:
            x = snake_head.xcor()
            y = snake_head.ycor()
            snake_tail[0].goto(x, y)

        snake_head.move()

        #check for head collision with snaketail
        for segment in snake_tail:
            if segment.distance(snake_head) < 20:
                reset_score()

                for segment in snake_tail:
                    segment.goto(1000,1000)
            
                snake_tail.clear()

                score = 0
        head.slow_game_down(0.1)

        score_display.clear()

def reset_score():
    snake_head.goto(0,0)
    winsound.PlaySound("restart_score.wav", winsound.SND_ASYNC)
    head.slow_game_down(1)

def gamecontrols():
    window.onkeypress(snake_head.move_up , "Up")
    window.onkeypress(snake_head.move_down, "Down")
    window.onkeypress(snake_head.move_right, "Right")
    window.onkeypress(snake_head.move_left, "Left")
    window.onkeypress(window.bye, 'Escape')

main()