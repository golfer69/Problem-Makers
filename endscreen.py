import tkinter as tk

def replay_game():
    end_screen.destroy()
    create_home_screen()

def enter_key(event):
    replay_game()

user_dict = {}

# Open and read the text file
with open('user_names.txt', 'r') as file:
    # Read all lines and populate the dictionary
    for line in file:
        user_name = line.strip()  # strip() removes leading and trailing whitespaces
        user_dict[user_name] = 0  # You can assign any value to the user, for example, True

end_screen = tk.Tk()
end_screen.geometry('600x400')
end_screen.title('Shapey')
table = tk.Label(end_screen, text=(user_dict))
table.pack(pady=20)
replay = tk.Button(end_screen, text=('Play Again'), font=('Arial', 20), command=replay_game)
replay.pack(pady=50)

end_screen.bind('<Return>', enter_key)
end_screen.mainloop()






