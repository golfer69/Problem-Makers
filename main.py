# *********************************************************
# Program: main.py
# Course: PSP0101 PROBLEM SOLVING AND PROGRAM DESIGN
# Class: TL9L
# Year: 2023/24 Trimester 1
# Names: ALIF AKMAL | SCHWEETA A P KUMARAN | BRIAN NG ZHENG YANG
# IDs: 1221109242 | 1221105995 | 1221109246
# Emails: 1221109242@student.mmu.edu.my | 1221105995@student.mmu.edu.my | 1221109246@student.mmu.edu.my
# Phones: +60 18-355 5944 | +60 16-207 2813 | +60 17-779 3199
# *********************************************************
import random
import tkinter as tk
from turtle import RawTurtle, TurtleScreen

#homescreen initialisation
with open("homescreen.py") as f:
    code = f.read()
exec(code)

# window
window = tk.Tk() 
window.title("Shapey | Quiz window")

# Create the Canvas for Turtle graphics
canvas = tk.Canvas(window, width=600, height=400)
canvas.pack()

# Link Turtle to the canvas in tkinter
screen = TurtleScreen(canvas)  # Link Turtle to the Canvas
t = RawTurtle(screen)  # Create a RawTurtle instance

## Shapes and colors ##

shapes = ["Square", "Circle", "Triangle","Hexagon"]
shape_1 = random.choice(shapes)
shape_2 = random.choice(shapes)
shape_3 = random.choice(shapes)
chosen_shapes = [shape_1, shape_2, shape_3] #Chooses types of shape for the question 

colors = ['red', 'blue', 'green','purple','yellow']

num_shapes = random.randint(1, 2)	#Chooses how many shapes will be drawn 

## Draw functions ## (Scheewta part)
t.speed(0) # makes it super fast

def draw_triangle(color): #Triangle
    t.penup()
    t.pencolor(color)
    t.fillcolor(color)
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

def draw_square(color): #Square
    t.penup
    t.pencolor(color)
    t.begin_fill()
    t.fillcolor(color)
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

def draw_circle(color): #Circle 
    r=30
    t.penup()
    t.pendown()
    t.pencolor(color)
    t.begin_fill()
    t.fillcolor(color)
    t.circle(r)
    t.end_fill()
    t.penup()
    t.hideturtle()

def draw_hexagon(color):
    t.penup()
    t.pencolor(color)
    t.begin_fill()
    t.fillcolor(color)
    t.pendown()
    for _ in range(6):
        t.forward(30)
        t.left(60)
    t.end_fill()
    t.penup()
    t.hideturtle()
   
## Coordinates ## (Scheewta part)
     
base_coordinates1 = (0, 0)
base_coordinates2 = (100, 0)

coordinates_list = [base_coordinates1,base_coordinates2]
## Drawing ##

def draw(shape,color): #Calls draw function
    if shape == "Triangle":
        draw_triangle(color)
    elif shape == "Square":
        draw_square(color)
    elif shape == "Circle":
        draw_circle(color)
    elif shape == "Hexagon":
       draw_hexagon(color)

## Quiz ##

# Random generator
shapes_data = {}

for _ in range(num_shapes):
    shape_type = random.choice(chosen_shapes)  # choose shape type

    # Check if shape_type is already in shapes_data
    if shape_type in shapes_data:
      print("added 1 already")
      shapes_data[shape_type]['amount'] += 1  # Increment count if shape exists
    else:
      color = random.choice(colors)  # choose color
      # Add new shape_type to shapes_data with count 1
      shapes_data[shape_type] = {'color': color, 'amount': 1}

print(shape_type)

print(shapes_data)
# Draw shapes
print(f"num_shapes: {num_shapes}")
if len(shapes_data) == 1: # if there's only one shape
  for shape_type in shapes_data:
      for coordinate in coordinates_list[:num_shapes]:
          print(f"Coordinate: {coordinate}")
          color = shapes_data[shape_type]['color']
          t.goto(coordinate)
          draw(shape_type, color)
else: 
  for coordinate, shape_type in zip(coordinates_list[:num_shapes],shapes_data):
      print(f"Coordinate: {coordinate}")
      color = shapes_data[shape_type]['color']
      t.goto(coordinate)
      draw(shape_type, color)
    
# Questions

def get_other_shapes(current_shape):
    available_shapes = list(shapes)
    available_shapes.remove(current_shape)
    random.shuffle(available_shapes)
    return available_shapes[:2]  # Choose 2 other shapes for answer options

def get_other_colors(current_color):
    available_colors = list(colors)
    available_colors.remove(current_color)
    random.shuffle(available_colors)
    return available_colors[:2]  # Choose 2 other shapes for answer options

questions = [] 
for index, (shape_type, shape_info) in enumerate(shapes_data.items()):
    other_shapes = get_other_shapes(shape_type)  # Call the function to get other shapes
    other_colors = get_other_colors(shape_info['color'])
    questions.append({
        "question": f"What is the #{index + 1} shape?",
        "answers": [shape_type, *other_shapes],  # Unpack other_shapes here
        "correct": [shape_type], 
    })
    questions.append({
      "question": f"How many {shape_type} are there?",
      "answers": ["1","2","3"],
      "correct": [str(shape_info['amount'])],
    })
    questions.append({
      "question": f"What is the color of #{index + 1} shape?",
      "answers": [str(shape_info['color']),*(get_other_colors(shape_info['color']))],
      "correct": (shape_info['color'])})

def next_question():
    global question_index, current_question, answer_buttons
    print(f"question_index: {question_index}")
    if question_index == 0: #To skip to the next question (only applies for first question)
        current_question = questions[question_index]
        question_label.config(text=current_question["question"]) #configure the label for question
        question_no_label.config(text="Question #"+ str((question_index+1))) #configure number of the question
        question_index += 1
        next_question()
    elif question_index == len(questions):  # end of quiz
      for button in answer_buttons:
        button.pack_forget() # Hide answer buttons temporarily
      question_label.config(text="") # clear labels
      question_no_label.config(text="")
      end_label.config(text="Quiz completed! Your score is " + str(score) + "/" + str(len(questions)))
    else:
        current_question = questions[question_index]
        question_label.config(text=current_question["question"]) #configure the label for question
        question_no_label.config(text="Question #"+ str((question_index+1))) #configure number of the question
        for i, answer in enumerate(current_question["answers"]):
          answer_buttons[i].config(text=answer)
        question_index += 1
        
# Prints question 
question_index = 0

current_question = questions[question_index] # shows which question are they on 
question_no_label= tk.Label(window, text="Question #"+ str((question_index+1)))
question_no_label.pack(pady=20) #show the widget 

question_label = tk.Label(window, text=current_question["question"])
question_label.pack(pady=20)

# Check ans and record score
score = 0
score_label = tk.Label(window, text="")
score_label.pack()
score_label.place(x=10, y=410)

def check_answer(index):
    selected_answer = answer_buttons[index].cget("text") # get the answer button's text 
    global score
    if selected_answer in current_question["correct"]:
        score += 100
        answered_shape = selected_answer # Store the correct shape
        print(f"Stored shape: {answered_shape}" ) 
    elif selected_answer != current_question['correct']: # skip next question if wrong ans
      score += 0
    elif int(selected_answer) == shape_amount:
      for shape_type, shape_info in shapes_data.items():
        if shape_type == answered_shape:
          shape_amount = shape_info['amount'] # Gets the value of the correct shape
      print(f"Value from dict: {shape_amount}") 
      score += 100
      print(f"Score: {score}")
    score_label.config(text= f"Score: {score}") # update the score 
    

# Create answers button and respond to clicked button

answer_buttons = [] # Create a list to append
for index, answers in enumerate(current_question["answers"]): 
  button = tk.Button(window, text=answers, command=lambda index=index: (check_answer(index), next_question())) 
  button.pack(pady=5)
  answer_buttons.append(button)

end_label = tk.Label(window, text="")
end_label.pack()

window.mainloop()

#endscreen initialisation
with open("endscreen.py") as f:
    code = f.read()
exec(code)
