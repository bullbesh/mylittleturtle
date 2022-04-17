"""Script with number of rainbow circles.

Each circle has different color and radius.
"""

import turtle
import time
from itertools import count


class ColoredCircle(turtle.Turtle):
    """Colored circle."""

    def __init__(self, bg: str, radius: int, stroke: int, velocity: int):
        super().__init__()
        self.bg = bg
        self.radius = radius
        self.stroke = stroke
        self.velocity = velocity
    
    def draw(self):
        """Draw itself."""
        self.begin_fill()
        self.speed(self.velocity)
        self.pensize(self.stroke)
        self.color(self.bg)
        self.circle(self.radius)
        self.end_fill()


class ColoredCircles:
    """Colored circles."""

    def __init__(self, circles: list[ColoredCircle]):
        self.circles = circles

    @classmethod
    def default(cls):
        """Create circles with default parameters."""
        colors = ["Red", "Orange", "Yellow", "Green", "Cyan", "Blue", "Purple"]
        radiuses = count(140, -20)
        circles = [
            ColoredCircle(color, radius, stroke=3, velocity=10)
            for (color, radius) in zip(colors, radiuses)
        ]
        return cls(circles)

    def draw(self):
        """Draw itself."""
        turtle.title("Rainbow Nested Circles")
        for circle in self.circles:
            circle.draw()


if __name__ == "__main__":
    ColoredCircles.default().draw()
    time.sleep(5)
