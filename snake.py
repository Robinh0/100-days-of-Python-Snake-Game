from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]
        self.tail = self.snake_body[-1]
        self.heading = "Right"

    def create_snake(self):
        for x, y in STARTING_POSITIONS:
            segment = Turtle('square')
            segment.penup()
            self.snake_body.append(segment)
            segment.color('white')
            pos = (x, y)
            segment.goto(pos)
            # print(self.snake_body)

    def move_forward(self):
        for i in range(len(self.snake_body) - 1, 0, -1):
            previous_segment = i - 1
            new_x = self.snake_body[previous_segment].xcor()
            new_y = self.snake_body[previous_segment].ycor()
            self.snake_body[i].goto(new_x, new_y)
        self.head.forward(20)

    def add_segment(self):
        segment = Turtle('square')
        segment.penup()
        segment.color('white')
        tail_x = self.tail.xcor()
        tail_y = self.tail.ycor()
        if self.heading == 'Up':
            pos = (tail_x, tail_y - 20)
        elif self.heading == 'Down':
            pos = (tail_x, tail_y + 20)
        elif self.heading == 'Left':
            pos = (tail_x + 20, tail_y)
        else:
            pos = (tail_x - 20, tail_y)
        segment.goto(pos)
        self.snake_body.append(segment)

    def check_game_over(self):
        if self.check_hit_wall() or self.check_hit_tail():
            return True
        else:
            return False

    def check_hit_wall(self):
        if self.head.xcor() > 280:
            return True
        elif self.head.xcor() < -280:
            return True
        elif self.head.ycor() > 280:
            return True
        elif self.head.ycor() < -280:
            return True
        else:
            return False

    def check_hit_tail(self):
        for segment in self.snake_body[1:]:
            if self.head.distance(segment) < 10:
                print('Hitting self as distance is getting lower!')
                return True

    def up(self):
        if self.heading != "Down":
            self.head.setheading(90)
            self.heading = "Up"

    def right(self):
        if self.heading != "Left":
            self.head.setheading(0)
            self.heading = "Right"

    def left(self):
        if self.heading != "Right":
            self.head.setheading(180)
            self.heading = "Left"

    def down(self):
        if self.heading != "Up":
            self.head.setheading(270)
            self.heading = "Down"
