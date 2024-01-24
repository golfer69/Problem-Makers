import tkinter as tk

def replay_game():
    end_screen.destroy()
    

def enter_key(event):
    replay_game()

end_screen=tk.Tk()
end_screen.geometry('600x400')
end_screen.title('Shapey')
table=tk.Label(end_screen, text=(database))
table.pack(pady=20)
replay=tk.Button(end_screen, text=('Play Again'), font=('Arial', 20), command=replay_game)
replay.pack(pady=50)

end_screen.bind('<Return>', enter_key)
end_screen.mainloop()


# name=tk.Label(end_screen, text='Enter your name', font=('Arial', 25))
# name.pack(pady=40)

# name_entry=tk.Entry(end_screen,)
# name_entry.pack(pady=10)

# enter_button=tk.Button(end_screen, text='Enter', font=('Helvetica', 15))
# enter_button.pack(pady=20)


# def insertkey():
#     return input("Enter your name: ")

# def insertvalue():
#     return int(input("Enter your score: "))

# # Call the functions to get user input
# name = insertkey()
# score = insertvalue()

# # Create the database dictionary using the obtained values
# database = {'Name': name, 'Score': score}

# # Function to insert new key-value pair
# def insert_new_data():
#     new_key = input("Enter your name (or type 'close' to stop): ")

#     # Check if the user wants to stop
#     if new_key.lower() == 'close':
#         return False

#     new_value = input("Enter your score: ")
#     database[new_key] = new_value
#     print(f"Data inserted: {new_key}: {new_value}")
#     return True

# # Continuously insert new data
# while insert_new_data():
#     pass

# print(database)




# def show_leaderboard():
#     print("Leaderboard:")
#     print("-------------")
#     for name, score in sorted(database.items(), key=lambda x: x[1], reverse=True):
#         print(f"{name}: {score}")

# def insert_new_data():
#     new_key = input("Enter your name (or type 'close' to stop): ")

#     # Check if the user wants to stop
#     if new_key.lower() == 'close':
#         return False

#     new_value = int(input("Enter your score: "))
#     database[new_key] = new_value
#     print(f"Data inserted: {new_key}: {new_value}")
#     return True

# # Database initialization
# database = {}

# # Continuously insert new data
# while insert_new_data():
#     pass

# # Show the leaderboard
# show_leaderboard()




