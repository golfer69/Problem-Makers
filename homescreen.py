# import tkinter as tk

# def showname():
#     enteredname = user.get()
#     greeting_label.config(text=f'Hello, {enteredname}!')

# home = tk.Tk()
# home.geometry('600x400')
# home.title('My Game')

# start = tk.Label(home, text='Welcome to our game!', font=('Helvetica', 16), fg='purple', bg='lightblue')
# start.pack(padx=10, pady=50)

# name = tk.Label(home, text='Enter your name below', font=('Lobster', 20))
# name.pack()

# user = tk.Entry(home, font=('Arial', 10))
# user.pack()

# enter = tk.Button(home, text='Enter', command=showname)
# enter.pack(pady=10)

# greeting_label = tk.Label(home, text='', font=('Arial', 14))
# greeting_label.pack(pady=20)

# database={'Name': ''}

# home.mainloop()



import tkinter as tk
import json

# def showname():
#     enteredname = user.get()
#     enteredscore= score.get()
#     greeting_label.config(text=f'Hello, {enteredname}!')
#     update_leaderboard(enteredname, enteredscore)  # You can initialize the score to 0 or any other default value

# def update_leaderboard(name, score):
#     database[name] = score
#     show_leaderboard()

# def show_leaderboard():
#     leaderboard_text.set("Leaderboard:\n" + "-------------\n" + "\n".join(f"{name}: {score}" for name, score in sorted(database.items(), key=lambda x: x[1], reverse=True)))

# def save_data_to_file():
#     with open('data.json', 'w') as file:
#         json.dump(database, file)

# def load_data_from_file():
#     try:
#         with open('data.json', 'r') as file:
#             return json.load(file)
#     except FileNotFoundError:
#         return {}

home = tk.Tk()
home.geometry('600x400')
home.title('My Game')

start = tk.Label(home, text='Welcome to our game!', font=('Helvetica', 16),)
start.pack(padx=10, pady=40)

game_name=tk.Label(home, text='Shapey', font=('Arial', 30), fg='purple', bg='lightblue')
game_name.pack(pady=10)

name_label = tk.Label(home, text='Enter your name', font=('Comic Sans MC', 20))
name_label.pack(pady=10)

user = tk.Entry(home, font=('Arial', 10))
user.pack(pady=10)

enter_button=tk.Button(home, text='Play', font=('Helvetica', 15),)
enter_button.pack(pady=10)

# score_label = tk.Label(home, text='Enter score below', font=('Comic Sans MC', 20))
# score_label.pack()

# score=tk.Entry(home, font=('Arial', 10))
# score.pack(pady=10)

# enter = tk.Button(home, text='Enter', command=showname)
# enter.pack(pady=10)

# greeting_label = tk.Label(home, text='', font=('Arial', 14))
# greeting_label.pack(pady=20)

# leaderboard_text = tk.StringVar()
# leaderboard_label = tk.Label(home, textvariable=leaderboard_text, font=('Arial', 12))
# leaderboard_label.pack(pady=10)

# database = load_data_from_file()

home.mainloop()