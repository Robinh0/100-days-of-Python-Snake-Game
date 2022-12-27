from turtle import Turtle
import random

x_ranges = range(-280,280, 20)
y_ranges = range(-280,280, 20)


class Food(Turtle):
    def __init__(self, snake_body):
        super().__init__()
        self.penup()
        self.color("green")
        self.shape('turtle')
        # self.shapesize(0.5)
        self.refresh(snake_body)

    def refresh(self, snake_body):
        looking_for_coords = True
        segment_coords = self.get_segment_coords(snake_body)
        while looking_for_coords:
            self.x_loc_food = random.choice(x_ranges)
            self.y_loc_food = random.choice(y_ranges)
            pos = self.x_loc_food, self.y_loc_food
            if pos not in segment_coords:
                looking_for_coords = False
        self.goto(pos)

    def get_segment_coords(self, snake_body):
        segment_coords = []
        for segment in snake_body:
            segment_x = segment.xcor()
            segment_y = segment.ycor()
            segment_coords.append((segment_x, segment_y))
        return segment_coords


