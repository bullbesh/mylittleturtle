import turtle
import time


t = turtle.Turtle()
turtle.title("Rainbow Nested Circles")
t.speed(10)
t.pensize(3)

circle_radius = [140, 120, 100, 80, 60, 40, 20]
circle_color = ["Red", "Orange", "Yellow", "Green", "Cyan", "Blue", "Purple"]

def create_circle_rainbow():
	for i, j in zip(circle_radius, circle_color):
		t.begin_fill()
		t.color(j)
		t.circle(i)
		t.end_fill()

if __name__ == "__main__":
	create_circle_rainbow()
	time.sleep(5)
