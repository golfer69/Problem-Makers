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

# Calculate the midpoint of the window for both the x and y coordinates
mid_x = end_screen.winfo_screenwidth() // 2
mid_y = end_screen.winfo_screenheight() // 2

#Making a full screen scroll bar
#create a main frame
end_frame=tk.Frame(end_screen)
end_frame.place(relx=0.5, rely=0.5, anchor='center')
#create a canvas
end_canvas=tk.Canvas(end_frame)
end_canvas.pack(side='left', fill='both', expand=True)

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

end_screen.geometry(f'600x400+{mid_x - 300}+{mid_y - 200}')


end_screen.bind('<Return>', enter3_key)
end_screen.mainloop()