# *********************************************************
# Program: game.py
# Course: PSP0101 PROBLEM SOLVING AND PROGRAM DESIGN
# Class: TL9L
# Year: 2023/24 Trimester 1
# Names: ALIF AKMAL | SCHWEETA A P KUMARAN | BRIAN NG ZHENG YANG
# IDs: 1221109242 | 1221105995 | 1221109246
# Emails: 1221109242@student.mmu.edu.my | 1221105995@student.mmu.edu.my | 1221109246@student.mmu.edu.my
# Phones: +60 18-355 5944 | +60 16-207 2813 | +60 17-779 3199
# *********************************************************
import random
import turtle

##Randomizer##

shapes = ["square", "circle", "triangle"]
random_shape = random.choice(shapes)

num_shapes=[1,2,3,4,5,6,7,8]
random_num_shapes = random.choice(num_shapes)

print("The randomly chosen shape is:", random_shape)
print(f"{random_num_shapes}")

##Shapes##

#Triangle

def draw_small_triangle(x, y, side_length):
  """
  Draws a small equilateral triangle at the specified location with the given side length.

  Args:
    x: The horizontal coordinate of the triangle's base center.
    y: The vertical coordinate of the triangle's base center.
    side_length: The length of one side of the triangle.
  """
  t = turtle.Turtle()
  t.penup()
  t.goto(x - side_length / 2, y)
  t.pendown()
  t.forward(side_length)
  t.left(120)
  t.forward(side_length)
  t.left(120)
  t.forward(side_length)
  t.penup()
  t.hideturtle()
#Square
def draw_square(x, y, side_length):
  t = turtle.Turtle()
  t.penup()
  t.goto(x - side_length / 2, y - side_length / 2)
  t.pendown()
  for _ in range(4):
    t.forward(side_length)
    t.left(90)
  t.penup()
  t.hideturtle()
#Cicle 
def draw_circle(x, y, radius):
  t = turtle.Turtle()
  t.penup()
  t.goto(x, y)
  t.pendown()
  t.circle(radius)
  t.penup()
  t.hideturtle()

##Draw##

if random_shape == "triangle":
  draw_small_triangle(0, 0, 50)
  turtle.done()
elif random_shape == "square":
  draw_square(0, 0, 50)
  turtle.done()
elif random_shape =="circle":
  draw_circle(0, 0, 25)
  turtle.done()