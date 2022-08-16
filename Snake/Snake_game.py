import turtle

width = 500
height = 500
Delay = 500

offsets = {
    "up" : [0, 20],
    "down" : [0, -20],
    "left" : [-20, 0],
    "right" : [20, 0],
}

def move_snake():
    stamper.clearstamps()

    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_directions][0]
    new_head[1] += offsets[snake_directions][1]
    snake.append(new_head)

    snake.pop(0)

    for segment in snake:
        stamper.goto(segment[0], segment[1])
        stamper.stamp()

    screen.update()

    turtle.ontimer(move_snake, Delay)

def go_up():
    global snake_directions
    if snake_directions != "down":
        snake_directions = "up" 

def go_down():
    global snake_directions
    if snake_directions != "up":
        snake_directions = "down"

def go_right():
    global snake_directions
    if snake_directions != "left":
        snake_directions = "right"

def go_left():
    global snake_directions
    if snake_directions != "right":
        snake_directions = "left"


screen = turtle.Screen()
screen.setup(width, height)
screen.title("Snake Game")
screen.bgcolor("pink")
screen.tracer(0)

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_right, "Right")
screen.onkey(go_left, "Left")

stamper = turtle.Turtle()
stamper.shape("square")
stamper.color("black")
stamper.penup()

snake = [[0, 0], [20, 0], [40, 0], [60, 0]]
snake_directions = "up"

for segment in snake:
        stamper.goto(segment[0], segment[1])
        stamper.stamp()

move_snake()


turtle.done()