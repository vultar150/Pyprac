from turtle import *
from random import *
from math import *


def fun():
	x = randint(-60, 60)
	while abs(x) < 20:
		x = randint(-60, 60)
	return x

def state(a, b):
	width, height = window_width(), window_height()
	maxX = width/2
	maxY = height/2
	if abs(a) > maxX or abs(b) > maxY:
		return True
	else:
		return False


N = 2000
pensize(2)
shape("turtle")
speed(12)

for i in range(N):
	if state(*pos()):
		d = atan(pos()[1]/pos()[0]) * 180 / pi
		right (180*(1+(pos()[0] < 0)) - d + heading())
		for j in range(4):
			circle((1 if j in {0,3} else -1)*randint(20,60), 90)
	else:
		circle(fun(), randint(10, 200))
		color(random(), random(), random())


exitonclick()
