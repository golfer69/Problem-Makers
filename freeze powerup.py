import tkinter

window = tkinter.Tk()

limit = 30
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

ScoreL = tkinter.Label(window, text=current_time)
ScoreL.pack()

window.after(1000, update) # start the update 1 second later
window.mainloop()