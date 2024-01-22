import tkinter as tk
import json

home = tk.Tk()
home.geometry('600x400')
home.title('Shapey')

start = tk.Label(home, text='Welcome to our game!', font=('Helvetica', 16),)
start.pack(padx=10, pady=40)

game_name=tk.Label(home, text='Shapey', font=('Arial', 30), fg='purple', bg='lightblue')
game_name.pack(pady=10)

name_label = tk.Label(home, text='Enter your name', font=('Comic Sans MC', 20))
name_label.pack(pady=10)

user = tk.Entry(home, font=('Arial', 10))
user.pack(pady=10)

play_button=tk.Button(home, text='Play', font=('Helvetica', 15))
play_button.pack(pady=40)

home.mainloop()