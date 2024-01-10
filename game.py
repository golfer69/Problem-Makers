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

## Randomizer ##

#Chooses types of shape for the question 
shapes = ["square", "circle", "triangle"]
shape_1 = random.choice(shapes)
shape_2 = random.choice(shapes)
shape_3 = random.choice(shapes)
chosen_shapes = [shape_1, shape_2, shape_3]

#Chooses how many shapes will be drawn 
random_num_shapes = random.randint(1, 2)	

## Draw functions ## ALL OF THESE DRAWINGS ARE JUST FOR TESTING, CAN CHANGE 
t = turtle.Turtle()
t.speed(0)
side_length = 50 #sample sidelength can change in the future
radius = 25
#Triangle
def draw_triangle():
  t.penup()
  t.pendown()
  t.forward(side_length)
  t.left(120)
  t.forward(side_length)
  t.left(120)
  t.forward(side_length)
  t.penup()
  t.hideturtle()
#Square
def draw_square():
  t.penup()
  t.pendown()
  for _ in range(4):
    t.forward(side_length)
    t.left(90)
  t.penup()
  t.hideturtle()
#Cicle 
def draw_circle():
  t.penup()
  t.pendown()
  t.circle(radius)
  t.penup()
  t.hideturtle()

# Shapes counter ##
shape_counter = {}  # Initialize an empty dictionary for counts

def count(shape_counter, shape):
    if shape in shape_counter:
        shape_counter[shape] += 1  # Add one count if shape exists
    else:
        shape_counter[shape] = 1  # Add shape with count 1 if new
    return shape_counter  # Return the updated dictionary
def printcount():
    print("Shape counts:")
    for shape, count in shape_counter.items():
     print(f"- {shape}: {count}")



## Coordinates ##
base_coordinates1 = (0, 0)
base_coordinates2 = (100, 0)

## Drawing ##
#Random pick chosen shapes and record the shape picked


# count(shape_counter, shape)

#Call draw function

def draw(chosen_shapes):
    """Draws a random shape from the given list of shapes."""

    shape = random.choice(chosen_shapes)

    if shape == "triangle":
        draw_triangle()
    elif shape == "square":
        draw_square()
    elif shape == "circle":
        draw_circle()
    count(shape_counter, shape)

if random_num_shapes == 1:
  t.goto(0,0)
  draw(chosen_shapes)
elif random_num_shapes == 2:
  t.goto(base_coordinates1[0], base_coordinates1[1])
  draw(chosen_shapes)
  t.goto(base_coordinates2[0], base_coordinates2[1])
  draw(chosen_shapes)

turtle.mainloop()
printcount()