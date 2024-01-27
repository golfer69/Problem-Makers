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
import sqlite3


# homescreen initialisation
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

shapes = ["Circle","Triangle","Square","Pentagon","Hexagon"]
shape_1 = random.choice(shapes)
shape_2 = random.choice(shapes)
shape_3 = random.choice(shapes)
chosen_shapes = [shape_1, shape_2, shape_3] #Chooses types of shape for the question 

colors = ['red', 'blue', 'green','purple','yellow']

num_shapes = random.randint(1, 6)	#Chooses how many shapes will be drawn 

generated_shapes ={}
def generate_shape(): # Generate shape & their own color 
  for _ in range(num_shapes): #  generate shape_type and color of it
    shape_type = random.choice(chosen_shapes) 
    color = random.choice(colors)
    generated_shapes[shape_type] = {"color": color}

generate_shape()

## Draw functions ## (Schweeta part)
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

def draw_pentagon(color):  # Pentagon
    t.penup()
    t.pencolor(color)
    t.begin_fill()
    t.fillcolor(color)
    t.pendown()
    for _ in range(5):
        t.forward(30)  
        t.left(72)  
    t.end_fill()
    t.penup()
    t.hideturtle()


def draw_hexagon(color): # Hexagon
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
  


## Coordinates ## (Schweeta part)
    

base_coordinates1 = (-200, 50)
base_coordinates2 = (-100,50)
base_coordinates3 = (0,50)
base_coordinates4 = (-200,-50)
base_coordinates5 = (-100,-50)
base_coordinates6 = (0,-50)

coordinates_list = [base_coordinates1,base_coordinates2,base_coordinates3,base_coordinates4,base_coordinates5,base_coordinates6] 

## Drawing ##


def draw(coordinate,shape,color): #Calls draw function
  t.goto(coordinate)
  if shape == "Triangle":
        draw_triangle(color)
  elif shape == "Square":
        draw_square(color)
  elif shape == "Circle":
        draw_circle(color)
  elif shape == "Pentagon":
      draw_pentagon(color)
  elif shape == "Hexagon":
      draw_hexagon(color)

shapes_data = {} # initialise a dict for counting

# Draw the shapes
def drawing():
  for coordinate in coordinates_list[:num_shapes]:
    print(f"Drawing on coordinate: {coordinate}")
    shape = random.choice(list(generated_shapes.keys()))
    shape_color = generated_shapes[shape]["color"]
    t.penup()
    draw(coordinate, shape, shape_color)
    shape_color = generated_shapes[shape]["color"]

    print(shape)

    if shape in shapes_data: # Check if shape_type is already in shapes_data
      shapes_data[shape]["amount"] += 1  # add one if it exists
      print(shapes_data[shape]["amount"])
    else:
      shapes_data[shape]= {"color": shape_color, "amount": 1}
  
  print(f"num_shapes: {num_shapes}")
  print(shapes_data)

drawing()

## Quiz ##

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

def get_other_number(answer):
    available_numbers = [1,2,3,4,5,6]
    available_numbers.remove(answer)
    random.shuffle(available_numbers)
    return available_numbers[:2]  # Choose 2 other shapes for answer options

questions = [] 
for index, (shape_type, shape_info) in enumerate(shapes_data.items()):
    other_shapes = get_other_shapes(shape_type)  # Call the function to get other shapes
    other_colors = get_other_colors(shape_info['color'])
    other_numbers= get_other_number(shape_info['amount'])
    questions.append({
        "question": f"What is the #{index + 1} shape?",
        "answers": [shape_type, *other_shapes],  # Unpack other_shapes here
        "correct": [shape_type], 
    })
    questions.append({
      "question": f"How many {shape_type} are there?",
      "answers": [str(shape_info['amount']), *other_numbers],
      "correct": [str(shape_info['amount'])],
    })
    questions.append({
      "question": f"What is the color of #{index + 1} shape?",
      "answers": [str(shape_info['color']),*(get_other_colors(shape_info['color']))],
      "correct": (shape_info['color'])})

game_finished= False

def next_question():
    global question_index, current_question, answer_buttons, game_finished
    print(f"question_index: {question_index}")
    if question_index == 0: #To skip to the next question (only applies for first question)
        current_question = questions[question_index]
        question_label.config(text=current_question["question"]) #configure the label for question
        question_no_label.config(text="Question #"+ str((question_index+1))) #configure number of the question
        question_index += 1
        next_question()
    elif question_index == len(questions):  # end of quiz
      game_finished= True
      for button in answer_buttons:
        button.pack_forget() # Hide answer buttons temporarily
      question_label.config(text="") # clear labels
      question_no_label.config(text="")
      end_label.config(text="Quiz completed! Your score is " + str(score) + "/" + str(len(questions)))
      end_button.pack()
    else:
        current_question = questions[question_index]
        question_label.config(text=current_question["question"]) #configure the label for question
        question_no_label.config(text="Question #"+ str((question_index+1))) #configure number of the question
        random.shuffle(current_question["answers"]) # shuffle answers
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

#Freeze powerup
current_time = 0
freeze = "yes"

def update():
  global current_time, freeze
  ScoreL.configure(text=current_time)
  if current_time < limit and freeze != "yes":
      current_time += 1
      window.after(1000, update) # schedule next update 1 second later 
  if freeze == "yes":
      current_time = current_time

ScoreL = tk.Label(window, text=current_time)
ScoreL.pack()

window.after(1000, update)

conn=sqlite3.Connection('user_data.db')
cursor=conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS user_data(
                Name PRIMARY KEY,
                Score INTEGER
)             
                """)

# Check ans and record score
score = 0
score_label = tk.Label(window, text="")
score_label.pack()
score_label.place(x=10, y=410)

#powerup_active will only be true if the game score is above 400
powerup_2x=False
powerup_gift=False

def activate_2x():
  if score>=400:
    powerup_2x=True

def activate_gift():
  score+=200
  powerup_gift=True
      



def check_answer(index):
    global score, powerup_2x, powerup_gift
    selected_answer = answer_buttons[index].cget("text") # get the answer button's text 
    if selected_answer in current_question["correct"]:
      if powerup_2x:
        score += 200
        powerup_2x=False
      else:
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
      if score>=1000:
         powerup_gift=False
         
         
    score_label.config(text= f"Score: {score}") # update the score



# Create answers button and respond to clicked button

answer_buttons = [] # Create a list to append
random.shuffle(current_question["answers"])
for index, answers in enumerate(current_question['answers']): 
  button = tk.Button(window, text=answers, command=lambda index=index: (check_answer(index), next_question())) 
  button.pack(pady=5)
  answer_buttons.append(button)

# #When 2x points button is pressed, the score will double for the next question
double_score =tk.Button(window, text=('2x points'), command=activate_2x)
double_score.pack(padx=50)

# #When gift button is pressed, the 200 points will be added to the final score
gift_score=tk.Button(window, text=('Gift'), command=activate_gift)
gift_score.pack(padx=50)

def end_game():
  window.destroy()
  
end_label = tk.Label(window, text='')
end_label.pack()
end_button=tk.Button(window, text='Done yet?', command=end_game)
end_button.pack_forget()
# end_button.pack()
window.mainloop()


# endscreen initialisation
with open("endscreen.py") as f:
   code = f.read()
exec(code)









