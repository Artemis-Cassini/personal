import turtle

screen = turtle.Screen()
screen.setup(500,500)
screen.tracer(0)
turtle.hideturtle()
turtle.speed(0)
turtle.bgcolor('black')

turtle.pensize(4)

turtle.color('light gray')
for x in range(-502,500,25):
    turtle.up()
    turtle.goto(x,-500)
    turtle.down()
    turtle.seth(90)
    turtle.fd(1000)

for y in range(-502,500,25):
    turtle.up()
    turtle.goto(-500,y)
    turtle.down()
    turtle.seth(0)
    turtle.fd(1000)

turtle.up()
for x in range(-502,500,25):
    for y in range(-502,500,25):
        turtle.goto(x,y)
        turtle.dot('white')
screen.update()
turtle.done ()