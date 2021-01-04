from turtle import Turtle, Screen

class Invader(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.showturtle()

    def command(self, str):
        print(str)
        eval('self.' + str)

