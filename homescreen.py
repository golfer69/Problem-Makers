import tkinter as tk
import sqlite3

conn=sqlite3.Connection('user_data.db')
cursor=conn.cursor()

import sqlite3

conn=sqlite3.Connection('user_data.db')
cursor=conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS user_data(
                Name PRIMARY KEY,
                Score INTEGER
)             
                """)




def play_game():
    user_name = user.get()
    if user_name:
        welcome_message = f"Welcome, {user_name}! Let's start playing Shapey!"
        start.config(text=welcome_message, font=('Helvetica', 16, 'italic'), fg='green')
        global saved_name
        saved_name = user_name
        cursor.execute("""INSERT INTO user_data (Name) 
                       VALUES (?)""", (saved_name,))
        conn.commit()
        home.destroy()
    else:
        start.config(text='Please enter your name!', font=('Helvetica', 16), fg='red')


# When press enter key, the game will start
def enterkey(event):
    play_game()

def create_home_screen():
    global home, user  # Declare home and user as global variables

 
home = tk.Tk()
home.geometry('600x400')
home.title('Shapey | Homescree')

start = tk.Label(home, text='Welcome to our game!', font=('Helvetica', 16))
start.pack(padx=10, pady=40)

game_name = tk.Label(home, text='Shapey', font=('Arial', 30), fg='purple', bg='lightblue')
game_name.pack(pady=10)

name_label = tk.Label(home, text='Enter your name', font=('Comic Sans MC', 20))
name_label.pack(pady=10)

user = tk.Entry(home, font=('Arial', 10))
user.pack(pady=10)

play_button = tk.Button(home, text='Play', font=('Helvetica', 15), command=play_game)
play_button.pack(pady=40)

# Bind enter key to enterkey function
home.bind('<Return>', enterkey)



home.mainloop()

