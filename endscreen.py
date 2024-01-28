import tkinter as tk
import sqlite3

conn=sqlite3.Connection('user_data.db')
cursor=conn.cursor()


def leaderboard():
    cursor.execute('SELECT * FROM user_data ORDER BY Score DESC')  # Order by score in descending order
    return cursor.fetchall() #Return content from database to leaderboard


def end_game():
    end_screen.destroy()

def enter3_key(event):
    end_game()

leaderboard_data=leaderboard()

#end screen window
end_screen = tk.Tk()
end_screen.geometry('600x400')
end_screen.title('Shapey | Endscreen')

#Making a full screen scroll bar
#create a main frame
end_frame=tk.Frame(end_screen)
end_frame.pack(fill='both', expand=1)

#create a canvas
end_canvas=tk.Canvas(end_frame)
end_canvas.pack(fill='both', expand=1)

#add a scrollbar to canvas
end_scrollbar=tk.Scrollbar(end_frame, orient='vertical', command=end_canvas.yview)
end_scrollbar.pack(side='right', fill='y')

#configure the canvas
end_canvas.configure(yscrollcommand=end_scrollbar.set)
end_canvas.bind('<Configure>', lambda e: end_canvas.configure(scrollregion=end_canvas.bbox('all')))

#create another frame inside the canvas
second_frame=tk.Frame(end_canvas)

#add that new frame to a window in the canvas
end_canvas.create_window((0,0), window=second_frame, anchor='nw')

#leaderboard
for index, (name, score) in enumerate(leaderboard_data, start=1):
    label = tk.Label(second_frame, text=f"{index}. {name}: {score}", font=('Arial', 16))
    label.pack(pady=10)

# close game after pressing enter
close_game = tk.Button(second_frame, text=('Press Enter to Close'), font=('Arial', 20), command=end_game)
close_game.pack(pady=50, side='bottom')


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

end_screen.bind('<Return>', enter3_key)
end_screen.mainloop()