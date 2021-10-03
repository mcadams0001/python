import turtle as turtle
t = turtle.Turtle()
side = int(input("enter a length:  "))
shape = int(input("enter number of sides: "))


for i in range(shape):
 # drawing a first side
  
  t.forward(side)
  t.left (360/shape) 

turtle.done()