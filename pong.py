import turtle as tl

class PONG:
    def __init__(self):
        self.create_window()
        self.leftpaddle()
        self.rightpaddle()
        self.create_ball()
        self.keys()
        self.game()

    def create_window(self):
        self.root = tl.Screen()
        self.root.title("Pong Game")
        self.root.bgcolor("yellow")
        self.root.setup(width=600, height=400)
        self.root.tracer(0)

    def leftpaddle(self):
        self.left_paddle = tl.Turtle()
        self.left_paddle.speed(0)
        self.left_paddle.shape('square')
        self.left_paddle.color('red')
        self.left_paddle.shapesize(stretch_wid=7, stretch_len=1.2)  # Fixed typo
        self.left_paddle.penup()
        self.left_paddle.goto(-280, 0)

    def rightpaddle(self):
        self.right_paddle = tl.Turtle()
        self.right_paddle.speed(0)
        self.right_paddle.shape('square')
        self.right_paddle.color('white')
        self.right_paddle.shapesize(stretch_wid=7, stretch_len=1.2)  # Fixed typo
        self.right_paddle.penup()
        self.right_paddle.goto(280, 0)  # Fixed x-coordinate for right paddle

    def create_ball(self):
        self.ball = tl.Turtle()
        self.ball.speed(0)
        self.ball.shape('circle')
        self.ball.color('green')
        self.ball.penup()
        self.ball.goto(0, 0)
        self.ball_direction_x = 0.9
        self.ball_direction_y = 0.9

    def left_paddle_up(self):
        y = self.left_paddle.ycor()
        if y < 160:  # Limit paddle movement
            self.left_paddle.sety(y + 20)

    def left_paddle_down(self):
        y = self.left_paddle.ycor()
        if y > -160:  # Limit paddle movement
            self.left_paddle.sety(y - 20)

    def right_paddle_up(self):
        y = self.right_paddle.ycor()
        if y < 160:  # Limit paddle movement
            self.right_paddle.sety(y + 20)

    def right_paddle_down(self):
        y = self.right_paddle.ycor()
        if y > -160:  # Limit paddle movement
            self.right_paddle.sety(y - 20)

    def keys(self):
        self.root.listen()
        self.root.onkeypress(self.left_paddle_up, "w")
        self.root.onkeypress(self.left_paddle_down, "s")
        self.root.onkeypress(self.right_paddle_up, "Up")
        self.root.onkeypress(self.right_paddle_down, "Down")

    def game(self):
        while True:
            self.root.update()

            # Ball movement
            self.ball.setx(self.ball.xcor() + self.ball_direction_x)
            self.ball.sety(self.ball.ycor() + self.ball_direction_y)

            # Ball collision with top and bottom walls
            if self.ball.ycor() > 190:
                self.ball.sety(190)
                self.ball_direction_y *= -1

            if self.ball.ycor() < -190:
                self.ball.sety(-190)
                self.ball_direction_y *= -1

            # Ball collision with left and right walls
            if self.ball.xcor() > 290:
                self.ball.goto(0, 0)
                self.ball_direction_x *= -1

            if self.ball.xcor() < -290:
                self.ball.goto(0, 0)
                self.ball_direction_x *= -1

            # Ball collision with paddles
            if (self.ball.xcor() > 260) and (self.ball.ycor() < self.right_paddle.ycor() + 50) and (self.ball.ycor() > self.right_paddle.ycor() - 50):
                self.ball.setx(260)
                self.ball_direction_x *= -1

            if (self.ball.xcor() < -260) and (self.ball.ycor() < self.left_paddle.ycor() + 50) and (self.ball.ycor() > self.left_paddle.ycor() - 50):
                self.ball.setx(-260)
                self.ball_direction_x *= -1

def main():
    PONG()

if __name__ == '__main__':
    main()