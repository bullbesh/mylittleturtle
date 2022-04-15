import turtle
import time


t = turtle.Turtle()
turtle.title("Rainbow Nested Circles")

def create_circle_rainbow():
	i = 140
	t.pensize(3)
	t.begin_fill()
	t.color("Red")
	t.circle(i)
	t.end_fill()
	t.begin_fill()
	t.color("Orange")
	t.circle(i-20)
	t.end_fill()
	t.begin_fill()
	t.color("Yellow")
	t.circle(i-40)
	t.end_fill()
	t.begin_fill()
	t.color("Green")
	t.circle(i-60)
	t.end_fill()
	t.begin_fill()
	t.color("Cyan")
	t.circle(i-80)
	t.end_fill()
	t.begin_fill()
	t.color("Blue")
	t.circle(i-100)
	t.end_fill()
	t.begin_fill()
	t.color("Purple")
	t.circle(i-120)
	t.end_fill()

if __name__ == "__main__":
	create_circle_rainbow()
	time.sleep(5)
