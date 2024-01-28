import tkinter as tk
import sqlite3

conn=sqlite3.Connection('user_data.db')
cursor=conn.cursor()

# from main import saved_score 
# def insert_score_to_database(saved_score):
#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS user_data(Name PRIMARY KEY,Score INTEGER)""")
#     # Insert the score into the database
#     cursor.execute("""INSERT INTO user_data (Score) 
#                           VALUES (?)""", (saved_score,))
#     conn.commit()
#     conn.close()


def leaderboard():
    cursor.execute('SELECT * FROM user_data ORDER BY Score DESC')  # Order by score in descending order
    return cursor.fetchall()


def end_game():
    end_screen.destroy()

def enter2_key(event):
    end_game()

leaderboard_data=leaderboard()
end_screen = tk.Tk()
end_screen.geometry('1500x1000')
end_screen.title('Shapey | Endscreen')

#create a main frame
end_frame=tk.Frame(end_screen)
end_frame.pack(fill='both')

# create a canvas
end_canvas=tk.Canvas(end_frame)
end_canvas.pack(fill='both')

# add a scrollbar to canvas
end_scrollbar=tk.Scrollbar(end_frame, orient='vertical', command=end_canvas.yview)
end_scrollbar.pack(side='right', fill='y')

# configure the canvas
end_canvas.configure(yscrollcommand=end_scrollbar.set)
end_canvas.bind('<Configure>', lambda e: end_canvas.configure(scrollregion=end_canvas.bbox('all')))

# create another frame inside the canvas
second_frame=tk.Frame(end_canvas)

# add that new frame to a window in the canvas
end_canvas.create_window((0,0), window=second_frame, anchor='nw')


for index, (name, score) in enumerate(leaderboard_data, start=1):
    label = tk.Label(second_frame, text=f"{index}. {name}: {score}", font=('Arial', 16))
    label.pack(pady=10)
replay = tk.Button(second_frame, text=('Press Enter to Close'), font=('Arial', 20), command=end_game)
replay.pack(pady=50, side='bottom')


# Calculate the midpoint of the window for both the x and y coordinates
mid_x = end_screen.winfo_screenwidth() // 2
mid_y = end_screen.winfo_screenheight() // 2

# Calculate the width and height of the window
win_width = end_screen.winfo_reqwidth()
win_height = end_screen.winfo_reqheight()

# Calculate the coordinates for the middle of the window
x = mid_x - (win_width // 2)
y = mid_y - (win_height // 2)

# Set the window to be positioned at the calculated coordinates
end_screen.geometry(f'+{x}+{y}')

end_screen.bind('<Return>', enter2_key)
end_screen.mainloop()