from turtle import Turtle, Screen

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake():
    def __init__(self):
        self.snake_segments = []
        self.create()
        self.head = self.snake_segments[0]

    def create(self):
        for pos in STARTING_POS:
            self.add_segment(pos)

    def add_segment(self, pos):
        segment = Turtle()
        segment.penup()
        segment.goto(pos)
        segment.shape("square")
        segment.color("white")
        self.snake_segments.append(segment)

    def extend(self):
        # add a new segment to the snake
        self.add_segment(self.snake_segments[-1].position())

    def move(self):
        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[seg_num - 1].xcor()
            new_y = self.snake_segments[seg_num - 1].ycor()
            self.snake_segments[seg_num].goto(new_x, new_y)
        self.snake_segments[0].forward(MOVE_DIST)

    def up(self):
        # the snake can't move backwards
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
