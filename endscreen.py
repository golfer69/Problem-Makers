import tkinter as tk

def replay_game():
    # Save the score before replaying the game
    save_to_text_file(saved_name, score)
    end_screen.destroy()
    create_home_screen()

def enter_key(event):
    replay_game()


user_dict = {}

# Open and read the text file
with open('user_scores.txt', 'r') as file:
    # Read all lines and populate the dictionary
    for line in file:
        user_info = line.strip().split(',')  # split the line into a list [name, score]
        user_name = user_info[0]
        user_score = int(user_info[1])
        user_dict[user_name] = user_score

end_screen = tk.Tk()
end_screen.geometry('600x400')
end_screen.title('Shapey')
table = tk.Label(end_screen, text=str(user_dict))
table.pack(pady=20)
replay = tk.Button(end_screen, text=('Play Again'), font=('Arial', 20), command=replay_game)
replay.pack(pady=50)

end_screen.bind('<Return>', enter_key)
end_screen.mainloop()






