from turtle import Turtle

STARTING_POS=[(0,0),(-20,0),(-40,0)]
MOVE_DIST=20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:

    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):

        for pos in STARTING_POS:
            self.add_segment(pos)
            

    def add_segment(self,pos):
        new_segment=Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(pos)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())
        
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head=self.segments[0]

    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):

            x_corr=self.segments[seg_num-1].xcor()
            y_corr=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(x_corr,y_corr)

        self.head.forward(MOVE_DIST)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
       if self.head.heading() != 180:
            self.head.setheading(0)
