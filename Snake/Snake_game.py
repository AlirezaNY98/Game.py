import turtle
import random


Width = 500
Height = 500
Delay = 100
Foodsize = 10
offsets = {
    "up" : [0, 20],
    "down" : [0, -20],
    "left" : [-20, 0],
    "right" : [20, 0],
}


def bind_direction_keys():
    screen.onkey(lambda: set_snake_direction("up"), "Up")
    screen.onkey(lambda: set_snake_direction("down"), "Down")
    screen.onkey(lambda: set_snake_direction("right"), "Right")
    screen.onkey(lambda: set_snake_direction("left"), "Left")

def set_snake_direction(direction):
    global snake_direction
    if direction == 'up':
        if direction != 'down':
            snake_direction == 'Up'
    elif direction == 'down':
        if direction != 'up':
            snake_direction == 'Down'
    elif direction == 'right':
        if direction != 'left':
            snake_direction == 'Right'
    elif direction == 'left':
        if direction != 'right':
            snake_direction == 'Left'


def game_loop():
    stamper.clearstamps()

    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_directions][0]
    new_head[1] += offsets[snake_directions][1]

    if new_head in snake or (new_head[0] < - Width / 2) or (new_head[0] > Width / 2) \
        or (new_head[1] < - Height / 2 )or (new_head[1] > Height / 2):
        reset()

    else:

        snake.append(new_head)

        if not food_collision():
            snake.pop(0)


        for segment in snake:
            stamper.goto(segment[0], segment[1])
            stamper.stamp()

        screen.title(f"Snake Game. Score:{score}")
        screen.update()

        turtle.ontimer(game_loop, Delay)


def food_collision():
    global food_pos, score

    if get_distance(snake[-1], food_pos) < 20:
        score += 1
        food_pos = get_random_food_pos()
        food.goto(food_pos)
        return True

    return False



def get_random_food_pos():
    x = random.randint(- Width / 2 + Foodsize, Width / 2 - Foodsize)
    y = random.randint(- Height / 2 + Foodsize, Width / 2 - Foodsize)

    return (x, y)

def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5

    return distance



def reset():
    global snake, food_pos, snake_directions, score
    snake = [[0, 0], [20, 0], [40, 0], [60, 0]]
    snake_directions = "up"
    score = 0
    food_pos = get_random_food_pos()
    food.goto(food_pos)
    game_loop()

screen = turtle.Screen()
screen.setup(Width, Height)
screen.title("Snake Game")
screen.bgcolor("pink")
screen.tracer(0)
screen.listen()
bind_direction_keys()

stamper = turtle.Turtle()
stamper.shape("square")
stamper.color("black")
stamper.penup()

food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.shapesize(Foodsize / 20)
food.penup()

reset()

turtle.done()