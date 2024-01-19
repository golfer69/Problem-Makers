import tkinter as tk

home=tk.Tk()
home.geometry('600x400')
home.title('My Game')


start=tk.Label(home, text='Welcome to our game!', font=('Helvetica', 16), fg='purple', bg='lightblue')
start.pack(padx=10, pady=50)

name=tk.Label(home, text='Enter your name below', font=('Lobster', 20))
name.pack()

user=tk.Entry(home, font=('Arial', 10))
user.pack()

enter=tk.Button(home, text='Enter')
enter.pack(pady=10)







home.mainloop()

