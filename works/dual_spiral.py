import turtle
import time


t = turtle.Turtle()
turtle.title("Dual Spiral")
turtle.bgcolor("Beige")
t.speed(1000)


def create_spiral():
    for i in range(120):
        t.color("Red")
        t.circle(i)
        t.color("Orange")
        t.circle(i * 0.8)
        t.left(3)
        t.backward(3)


if __name__ == "__main__":
    create_spiral()
    time.sleep(5)
