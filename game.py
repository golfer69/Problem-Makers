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
import tkinter as tk

## Randomizer ##

#Chooses types of shape for the question 
shapes = ["Square", "Circle", "Triangle"]
shape_1 = random.choice(shapes)
shape_2 = random.choice(shapes)
shape_3 = random.choice(shapes)
chosen_shapes = [shape_1, shape_2, shape_3]

#Chooses how many shapes will be drawn 
random_num_shapes = random.randint(1, 2)	

## Draw functions ## 
t = turtle.Turtle()
t.speed(0)
side_length = 50 #sample sidelength can change in the future
radius = 25
#Triangle
def draw_triangle():
  #dont change the function name, just the code below
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

#Call draw function

def draw(chosen_shapes):
    """Draws a random shape from the given list of shapes."""

    shape = random.choice(chosen_shapes)

    if shape == "Triangle":
        draw_triangle()
    elif shape == "Square":
        draw_square()
    elif shape == "Circle":
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
  
## Quiz ##

# window and score
window = tk.Tk()
window.geometry("500x300")
window.title("Shapey | Quiz window")
score = 0
questions = [
    {"question": "What shape is it?", "answers": ["Triangle","Circle","Square"], "correct": list(shape_counter.keys())[0]},
]
#prints question 
question_index = 0
current_question = questions[question_index]
question_label = tk.Label(window, text=current_question["question"])
question_label.pack(pady=20)
#create answers button and respond to clicked button
answer_buttons = []
for answer in questions[0]["answers"]: 
   button = tk.Button(window, text=answer, command=lambda text=answer, score=score: check_answer(text, score))
   button.pack(pady=5)
   answer_buttons.append(button)
#check ans
def check_answer(text, score):
    if text == questions[0]["correct"]:
        score += 1
        print("congrats ig LOL")
        print(score)
    else:
       print(text)
       print(f"the ans is {questions[0]["correct"]}" )

window.mainloop()
printcount()
turtle.mainloop()

