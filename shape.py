
import random
import turtle
# making turtle work
t = turtle.Turtle()
t.speed(0) #
#drawing a triangle

#triangle
def draw_triangle():
   
  t.penup()
  t.pencolor("red")
  t.fillcolor("red")
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
def draw_circle():

    r=30
    t.penup()
    t.pendown()
    t.pencolor('orange')
    t.begin_fill()
    t.fillcolor('orange')
    t.circle(r)
    t.end_fill()
    t.penup()
    t.hideturtle()


#draw square 
def draw_square():
      
      t.pencolor("yellow")
      t.begin_fill()
      t.fillcolor("yellow")
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

 #draw pentagon 
def draw_pentagon():
            
            t.pencolor("green")
            t.begin_fill()
            t.fillcolor("green")
            t.pendown()
            for i in range (5):
                t.left(72)
                t.forward(40)
                t.left(72)
                t.forward(40)
                t.left(72)
                t.forward(40)
                t.left(72)
                t.forward(40)
                t.left(72)
                t.forward(40)
                t.end_fill()
                t.penup()
                t.hideturtle()
       
  #draw hexagon 
def draw_hexagon():

        
        t.pencolor("blue")
        t.begin_fill()
        t.fillcolor("blue")
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
       


shapes = ["Triangle", "Circle", "Square","Pentagon","Hexagon"]
shape_1 = random.choice(shapes) # selects the type of shapes that will be given for the question
shape_2 = random.choice(shapes)
shape_3 = random.choice(shapes)
shape_4 = random.choice(shapes)
shape_5 = random.choice(shapes)
chosen_shapes = [shape_1, shape_2, shape_3, shape_4, shape_5] 

shape_counter={}

def count(shape_counter, shape):
    if shape in shape_counter:
        shape_counter[shape] += 1  # add one if the shapes exist
    else:
        shape_counter[shape] = 1  # add another number 1 for another shape
    return shape_counter  # Return the updated dictionary
def printcount():
    print("Shape counts:")
    for shape, count in shape_counter.items():
     print(f"- {shape}: {count}")


shape = random.choice(chosen_shapes)
def draw (chosen_shapes):
 if shape =="Triangle" :
    draw_triangle ( )
 elif shape == "Circle" :  
    draw_circle()
 elif shape == "Square" :
    draw_square ()
 elif shape == "Pentagon":
     draw_pentagon()
 elif shape == "Hexagon" : 
     draw_hexagon() 

count(shape_counter,shape)


#Chooses how many shapes will be drawn 
random_num_shapes = random.randint(1,2)

base_coordinates1=(0,0)
base_coordinates2=(100,0)
if random_num_shapes == 1: # Go to different coordinates depending on the number of shapes
  t.goto (0,0)
  draw(chosen_shapes)
elif random_num_shapes == 2:
  t.goto(base_coordinates1[-7], base_coordinates1[0])
  draw(chosen_shapes)
  t.goto(base_coordinates2[-7], base_coordinates2[3])
  draw(chosen_shapes)
  t.goto(base_coordinates2[-3], base_coordinates2[0])
  draw(chosen_shapes)
  t.goto(base_coordinates2[-3], base_coordinates2[3])
  draw(chosen_shapes)
  t.goto(base_coordinates2[1], base_coordinates2[0])
  draw(chosen_shapes) 
  t.goto(base_coordinates2[1], base_coordinates2[3])
  draw(chosen_shapes)  
  t.goto(base_coordinates2[5], base_coordinates2[0])
  draw(chosen_shapes)
  t.goto(base_coordinates2[5], base_coordinates2[3])
  draw(chosen_shapes) 
            

               