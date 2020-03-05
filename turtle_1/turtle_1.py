from turtle import *
from random import *
reset()
shape("turtle")
color("red")

for i in range(20):
    forward(randint(0,100))
    if i%10:
    	right(randint(0,90))
    else:
    	left(randint(0,30))

mainloop()


