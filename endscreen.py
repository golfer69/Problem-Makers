import tkinter as tk
import json

end_screen=tk.Tk()
end_screen.geometry('600x400')
end_screen.title('Shapey')

name=tk.Label(end_screen, text='Enter your name', font=('Arial', 25))
name.pack(pady=40)

end_screen.mainloop()


