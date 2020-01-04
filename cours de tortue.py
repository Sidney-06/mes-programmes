from turtle import *
from random import randint

speed(0)
penup()
goto(-140,140)

for etape in range(15):
  write(etape, align='center')
  right(90)
  forward(10)
  pendown()
  forward(150)
  penup()
  backward(160)
  left(90)
  forward(20
  
ada = Turtle()
ada.color('red')
ada.shape('turtle')

ada.penup()
ada.goto(-160, 100)
ada.pendown()

bob = Turtle()
bob.color('blue')
bob.shape('turtle')

bob.penup()
bob.goto(-160, 70)
bob.pendown()

wil = Turtle()
wil.color('black')
wil.shape('turtle')

wil.penup()
wil.goto(-160, 40)
wil.pendown()

bil = Turtle()
bil.color('orange')
bil.shape('turtle')

bil.penup()
bil.goto(-160, 10)
bil.pendown()

for turn in range(1):
    ada.right(360)
    bob.left(360)
    wil.right(360)
    bil.left(360)

for tourner in range(100):
    ada.forward(randint(1,5))
    bob.forward(randint(1,5))
    wil.forward(randint(1,5))
    bil.forward(randint(1,5))
    
