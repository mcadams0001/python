import turtle
import random

colours = ["cyan","purple","white","blue"]

turtle.Screen().bgcolor("blue")

pat = turtle.Turtle()
pat.color(random.choice(colours))
for i in range(10):
    for i in range(2):
            pat.forward(100)
            pat.right(60)
            pat.forward(100)
            pat.right(120)
    pat.right(36)
