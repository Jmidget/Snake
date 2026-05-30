from turtle import Turtle, Screen
class Snake:
    def __init__(self):
        self.tail = []
        self.pos = []
        self.birth()
        self.screen = Screen()
        self.slither()
	
	# Initial setup for the snake with 3 segments
    def birth(self):
        for x in range(0, 3):
            self.tail.append(Turtle(shape='square'))
            self.tail[x].penup()
            self.tail[x].color('white')
            self.tail[x].goto(x=0 - (20 * x), y=0)

	# Growth function that adds a new segment every time the food item is 'touched' by the snake
    def evolve(self):
            self.tail.append(Turtle(shape='square'))
            self.tail[-1].penup()
            self.tail[-1].color('white')
            self.tail[-1].goto(x=self.pos[-1]['x'], y=self.pos[-1]['y'])
	
	# Function to get all segments to move one after another
	# definitely an easier way to do this, think backwards next time when doing a newx, newy
    def move(self):
        for r in range(0, len(self.tail)):
            self.pos.append({'x': self.tail[r].xcor(), 'y': self.tail[r].ycor()})
        for x in range(0, len(self.tail )):
            if x == 0:
                self.tail[x].forward(20)
            elif x != 0:
                self.tail[x].goto(x=self.pos[x - 1]['x'], y=self.pos[x - 1]['y'])
        for r in range(0, len(self.tail)):
            self.pos[r]['x'] =  self.tail[r].xcor()
            self.pos[r]['y'] =  self.tail[r].ycor()
    
	# Control Functions
    def turn_cclock(self):
        self.tail[0].left(90)

    def turn_clock(self):
        self.tail[0].right(90)

	# Control Functions implemented
    def slither(self):
        self.screen.onkey(key='Left', fun=self.turn_cclock)
        self.screen.onkey(key='Right', fun=self.turn_clock)
	
	# Reset function for the snake when a 'game over' event occurs
    def reset(self):
        for x in self.tail:
            x.goto(1000,1000)
        self.tail.clear()
        self.birth()