import tkinter as tk
import sqlite3

conn=sqlite3.Connection('user_data.db')
cursor=conn.cursor()

def leaderboard():
    cursor.execute('SELECT * FROM user_data ORDER BY Score DESC')  # Order by score in descending order
    return cursor.fetchall()


def replay_game():
    end_screen.destroy()

def enter2_key(event):
    replay_game()

leaderboard_data=leaderboard()

end_screen = tk.Tk()
end_screen.geometry('1500x1000')
end_screen.title('Shapey | Endscreen')
for index, (name, score) in enumerate(leaderboard_data, start=1):
    label = tk.Label(end_screen, text=f"{index}. {name}: {score}", font=('Arial', 16))
    label.pack(pady=10)
replay = tk.Button(end_screen, text=('Press Enter to Close'), font=('Arial', 20), command=replay_game)
replay.pack(pady=50)

end_screen.bind('<Return>', enter2_key)
end_screen.mainloop()






