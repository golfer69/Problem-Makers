import turtle
# making turtle work
t = turtle.Turtle()

#drawing the square 
t.speed(1)
t.penup()
t.goto(-80,100)
t.pendown()
t.color('black')

t.forward(80)
t.left(90)
t.forward(80)
t.left(90)
t.forward(80)
t.left(90)
t.forward(80)
t.left(90)
t.penup()
t.hideturtle()

# using a for loop 
t.goto(20,100)
t.color('black')
t.pendown()
for i in range(4) :
  t.forward(80)
  t.left(90)
t.penup()
