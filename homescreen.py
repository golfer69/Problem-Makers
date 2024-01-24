import tkinter as tk

# # database for leaderboard tracking
# database_file='database.json'

# def save_data():
#     with open(database_file, 'w') as file:
#         json.dump(database, file)

# def load_data():
#     try:
#         with open(database_file, 'r') as file:
#             data = json.load(file)
#             return data
#     except FileNotFoundError:
#         return {}

# database=load_data()

# def save_name_to_file(file_path, name):
#     with open(file_path, 'a') as file:
#         file.write(name + '\n')

# def read_names_from_file(file_path):
#     try:
#         with open(file_path, 'r') as file:
#             names = [line.strip() for line in file.readlines()]
#         return names
#     except FileNotFoundError:
#         return []

database={}
def play_game():
    user_name = user.get()
    if user_name:
        welcome_message = f"Welcome, {user_name}! Let's start playing Shapey!"
        start.config(text=welcome_message, font=('Helvetica', 16, 'italic'), fg='green')
        global saved_name
        saved_name = user_name
        database[saved_name] = {'name': saved_name, 'score': 0}
        home.destroy()
    else:
        start.config(text='Please enter your name!', font=('Helvetica', 16), fg='red')

# When press enter key, the game will start
def enterkey(event):
    play_game()
 
saved_name=""
names_file = "user_names.txt"
home = tk.Tk()
home.geometry('600x400')
home.title('Shapey')

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

