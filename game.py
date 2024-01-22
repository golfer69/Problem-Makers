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
from turtle import RawTurtle, TurtleScreen

# window and score
window = tk.Tk()
window.title("Shapey | Quiz window")
# Create the Canvas for Turtle graphics
canvas = tk.Canvas(window, width=600, height=400)
canvas.pack()

# Link Turtle to the Canvas
screen = TurtleScreen(canvas)  # Link Turtle to the Canvas
t = RawTurtle(screen)  # Create a RawTurtle instance

## Randomizer ##

#Chooses types of shape for the question 
shapes = ["Square", "Circle", "Triangle"]
shape_1 = random.choice(shapes)
shape_2 = random.choice(shapes)
shape_3 = random.choice(shapes)
chosen_shapes = [shape_1, shape_2, shape_3]

#Chooses how many shapes will be drawn 
random_num_shapes = random.randint(1, 2)	

## Draw functions ## (Scheewta part)
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
  t.end_fill()
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

## Coordinates ## (Scheewta part)
     
base_coordinates1 = (0, 0)
base_coordinates2 = (100, 0)


## Drawing ##

def draw(chosen_shapes): #Call draw function
    """Draws a random shape from the given list of shapes."""

    shape = random.choice(chosen_shapes)
    if shape == "Triangle":
        draw_triangle()
    elif shape == "Square":
        draw_square()
    elif shape == "Circle":
        draw_circle()
    count(shape_counter, shape)

if random_num_shapes == 1: # Go to different coodirnates depend on the number of shapes
  t.goto(0,0)
  draw(chosen_shapes)
elif random_num_shapes == 2:
  t.goto(base_coordinates1[0], base_coordinates1[1])
  draw(chosen_shapes)
  t.goto(base_coordinates2[0], base_coordinates2[1])
  draw(chosen_shapes)
  
## Quiz ##

<<<<<<< HEAD



=======
# Questions

def get_other_shapes(current_shape):
    available_shapes = list(shapes)
    available_shapes.remove(current_shape)
    random.shuffle(available_shapes)
    return available_shapes[:2]  # Choose 2 other shapes for answer options

questions = [] 
for index, (shape, count) in enumerate(shape_counter.items()):
    other_shapes = get_other_shapes(shape)  # Call the function to get other shapes
    questions.append({
        "question": f"What is the #{index + 1} shape?",
        "answers": [shape, *other_shapes],  # Unpack other_shapes here
        "correct": [shape], 
    })
    questions.append({
      "question": f"How many {shape} are there?",
      "answers": ["1","2","3"],
      "correct": [str(count)],
    })

# questions = [
#     {"question": "What shape is it?", "answers": ["Triangle","Circle","Square"], 
#      "correct": list(shape_counter.keys())},
#     {"question": "How many are there?", "answers": ["1","2","3"], 
#      "correct": list(shape_counter.values())}
# ]

# Function to show next question
    
def next_question():
    global question_index, current_question, answer_buttons
    print(f"question_index: {question_index}")
    if question_index == 0: #To skip to the next question (only applies for first question)
        current_question = questions[question_index]
        question_label.config(text=current_question["question"]) #configure the label for question
        question_no_label.config(text="Question #"+ str((question_index+1))) #configure number of the question
          # answer_buttons[i].config(text=answer)
        question_index += 1
        next_question()
    elif question_index == len(questions):  # Show score and end quiz  
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
def check_answer(index):
    selected_answer = answer_buttons[index].cget("text")
    print("Answer checked")
    global score
    if selected_answer in current_question["correct"]:
        score += 1
        print(f"Score: {score}")
        print(f"the answer is {selected_answer}")
        answered_shape = selected_answer # Store the correct shape
        print(f"Stored shape: {answered_shape}" ) 
        value_from_dict = shape_counter.get(answered_shape) # Gets the value of the shape
        print(f"Value from dict: {value_from_dict}") 
    elif int(selected_answer) == value_from_dict:
      print(f"Value of correct shape is: {value_from_dict}" )
      score += 1
      print(f"Score: {score}")
    else:
       print(selected_answer)
       print(f"the ans is {current_question["correct"]}" )

# Create answers button and respond to clicked button

answer_buttons = [] # Create a list to append
for index, answers in enumerate(current_question["answers"]): 
  button = tk.Button(window, text=answers, command=lambda index=index: (check_answer(index), next_question())) 
  button.pack(pady=5)
  answer_buttons.append(button)

end_label = tk.Label(window, text="")
end_label.pack()

window.mainloop()
>>>>>>> 4e753ae7b0d67d37e82aa856d5a61a9a10f10699
printcount()

