from turtle import Turtle
class Score:
    def __init__(self):
        self.turtle = Turtle()
        self.turtle.penup()
        self.turtle.pencolor('white')
        self.turtle.goto(x=0, y=270)
        self.turtle.ht()
        self.score = 0
        with open('high_score.txt', mode='r') as file:
            self.high_score = int(file.read())
        self.turtle.write(f'Score = {self.score} {' ' * 2}High Score = {self.high_score} ', align='center', font=('CenturyGothic', 15, 'bold'))

	# Score & High Score Display Setup
    def point(self):
        self.turtle.clear()
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
        self.turtle.write(f'Score = {self.score} {' ' * 2}High Score = {self.high_score} ', align='center', font=('CenturyGothic', 15, 'bold'))

	# Reset function for the scorew when a 'game over' event occurs
    def reset(self):
        self.turtle.clear()
        self.score = 0
        self.turtle.write(f'Score = {self.score} {' ' * 2}High Score = {self.high_score} ', align='center',font=('CenturyGothic', 15, 'bold'))
        with open('high_score.txt', mode='w') as file:
            file.write(f'{self.high_score}')
