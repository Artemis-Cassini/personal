import turtle
import turtle as t

t=t.Turtle()

turtle.title('Sixteen Petals Flower')



def draw_flower(x, y, tilt, radius):
    t.up()
    t.goto(x, y)
    t.down()
    t.seth(tilt-45)
    t.circle(radius, 90)
    t.left(90)
    t.circle(radius, 90)

for tilt in range(0, 360, 30):
    draw_flower(0, 0, tilt, 1000)

hideturtle () # type: ignore
done () # type: ignore