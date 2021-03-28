from turtle import * 
from random import randint

speed(0)
penup()
goto(-140, 140)

for step in range(6): 
  write(step, align='center')
  right(90)
  forward(10)
  pendown()
  forward(15)
  penup()
  forward(10)
  pendown()
  forward(15)
  penup()
  forward(10)
  pendown()
  penup()
  forward(15)
  pendown()
  penup()
  forward(15)
  pendown()
  penup()
  forward(15)
  penup()
  forward(15)
  penup()
  forward(15)
  penup()
  forward(15)
  penup()
  forward(15)
  penup()
  backward(160)
  left(90)
  forward(20)
  
ada = Turtle()
ada.color('dark slate blue')
ada.shape('turtle')

ada.penup()
ada.goto(-160, 100)
ada.pendown()

bob = Turtle()
bob.color('gold')
bob.shape('turtle')

bob.penup()
bob.goto(-160, 70)
bob.pendown()

tim = Turtle()
tim.color('lime green')
tim.shape('turtle')

tim.penup()
tim.goto(-160, 40)
tim.pendown()

claire = Turtle()
claire.color('orange red')
claire.shape('turtle')

claire.penup()
claire.goto(-160, 10)
claire.pendown()

for turn in range(100):
  ada.right(360)
  claire.right(360)
  bob.right(360)
  tim.right(360)
  break
  
for turn in range(100):
  ada.forward(randint(1,5))
  bob.forward(randint(1,5))
  tim.forward(randint(1,5))
  claire.forward(randint(1,5))
  bob.forward(randint(1,5))
