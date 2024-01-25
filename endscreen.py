import tkinter as tk

def replay_game():
    end_screen.destroy()
    

def enter_key(event):
    replay_game()


user_dict = {}

# Open and read the text file
with open('user_names.txt', 'r') as file_names, open('user_scores.txt', 'r') as file_scores:
    for name, score in zip(file_names, file_scores):
        user_name = name.strip()
        user_scores = int(score)
        user_dict[user_name] = user_scores



end_screen = tk.Tk()
end_screen.geometry('1500x1000')
end_screen.title('Shapey')
table = tk.Label(end_screen, text=str(user_dict))
table.pack(pady=20)
replay = tk.Button(end_screen, text=('Play Again'), font=('Arial', 20), command=replay_game)
replay.pack(pady=50)

end_screen.bind('<Return>', enter_key)
end_screen.mainloop()






