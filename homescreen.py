import tkinter as tk

user_name=" "
def play_game():
    global user_name #to be used in main.py
    if user_name:
        user_name = user.get()
        home.destroy()
    else:
        start.config(text='Please enter your name!', font=('Helvetica', 16), fg='red') #if no name is entered, a message in red will show up


# When press enter key, the game will start
def enterkey(event):
    play_game()

  # Declare home and user as global variables

 
home = tk.Tk()
home.geometry('600x400')
home.title('Shapey | Homescreen')

start = tk.Label(home, text='Welcome to our game!', font=('Helvetica', 16))
start.pack(padx=10, pady=40)

game_name = tk.Label(home, text='Shapey', font=('Arial', 30), fg='purple', bg='lightblue')
game_name.pack(pady=10)

name_label = tk.Label(home, text='Enter your name', font=('Comic Sans MC', 20))
name_label.pack(pady=10)

user = tk.Entry(home, font=('Arial', 10))
user.pack(pady=10)


play_button = tk.Button(home, text='Enter', font=('Helvetica', 15), command=play_game)
play_button.pack(pady=40)


# Bind enter key to enterkey function
home.bind('<Return>', enterkey)

home.mainloop()

