# Write your code here :-)
from turtle import Turtle, Screen

t: str = Turtle()
s = Screen()

s.bgcolor("black")
t.speed(0)
t.color("cyan")

for i in range(1000):
    t.forward(150)
    t.right(88)
