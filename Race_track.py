from turtle import * 
from random import randint
"""
write(0) 
forward(20) 
write(1) 
forward(20) 
write(2) 
forward(20) 
write(3) 
forward(20) 
write(4) 
forward(20) 
write(5) 
forward(20) 
"""
speed(0)
penup()
goto(-140, 140)

for step in range(6): 
  write(step, align='center')
  right(90)
  forward(10)
  pendown()
  forward(150)
  penup()
  backward(160)
  left(90)
  forward(20)
  
ada = Turtle()
ada.color('red')
ada.shape('turtle')

ada.penup()
ada.goto(-160, 100)
ada.pendown()

bob = Turtle()
bob.color('yellow')
bob.shape('turtle')

bob.penup()
bob.goto(-160, 70)
bob.pendown()

tim = Turtle()
tim.color('green')
tim.shape('turtle')

tim.penup()
tim.goto(-160, 40)
tim.pendown()

claire = Turtle()
claire.color('orange')
claire.shape('turtle')

claire.penup()
claire.goto(-160, 10)
claire.pendown()

for turn in range(100):
  ada.forward(randint(1,5))
  bob.forward(randint(1,5))
  tim.forward(randint(1,5))
  claire.forward(randint(1,5))
  bob.forward(randint(1,5))