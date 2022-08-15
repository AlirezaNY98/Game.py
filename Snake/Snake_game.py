import turtle

width = 500
height = 500
Delay = 400

def move_snake():
    stamper.clearstamps()

    new_head = snake[-1].copy()
    new_head[0] += 20
    snake.append(new_head)

    snake.pop(0)

    for segment in snake:
        stamper.goto(segment[0], segment[1])
        stamper.stamp()

    screen.update()

    turtle.ontimer(move_snake, Delay)

screen = turtle.Screen()
screen.setup(width, height)
screen.title("Snake Game")
screen.bgcolor("pink")
screen.tracer(0)

stamper = turtle.Turtle()
stamper.shape("square")
stamper.color("black")
stamper.penup()

snake = [[0, 0], [20, 0], [40, 0], [60, 0]]

for segment in snake:
        stamper.goto(segment[0], segment[1])
        stamper.stamp()

move_snake()

turtle.done()