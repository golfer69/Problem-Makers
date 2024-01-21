import turtle
# making turtle work
t = turtle.Turtle()

#drawing a triangle

t.penup()
t.goto(-130,5)
t.pencolor("lime green")
t.fillcolor("lime green")
t.begin_fill()
t.pendown()
t.forward(60)
t.left(120)
t.forward(60)
t.left(120)
t.forward(60)
t.left(120)
t.end_fill()
t.penup()
t.hideturtle()

#draw circle
r=30
t.goto(-30,5)
t.penup()
t.pendown()
t.pencolor('blue')
t.begin_fill()
t.fillcolor('blue')
t.circle(r)
t.end_fill()
t.penup()
t.hideturtle()

#draw square 
t.goto(30,5)
t.pencolor("orange")
t.begin_fill()
t.fillcolor("orange")
t.pendown()
for i in range (4):
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.end_fill()
    t.penup()
    t.hideturtle()

  #draw hexagon 
    t.goto(130,5)
    t.pencolor("purple")
    t.begin_fill()
    t.fillcolor("purple")
    t.pendown()
    for i in range (6):
        t.forward(30)
        t.left(60)
        t.forward(30)
        t.left(60)
        t.forward(30)
        t.left(60)
        t.forward(30)
        t.left(60)
        t.forward(30)
        t.left(60)
        t.forward(30)
        t.left(60)
        t.end_fill()
        t.penup()
        t.hideturtle()

