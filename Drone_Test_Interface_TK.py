import tkinter as tk
from tkinter import *

class Drone:
    def __init__(self, root):
        self.root = root
        self.root.title("Drone")
        self.root.title("Drone Test Interface")
        self.root.geometry("800x600")
        self.canvas = tk.Canvas(self.root, bg="black")
        self.canvas.grid(row=1, column=0, columnspan=5, sticky="nsew")
        self.create_widgets()

    def create_widgets(self):
        self.funclabel = tk.Label(root, text='Enter Data 1')
        self.funclabel.place(x=0, y=0)

        self.entry1 = tk.Entry(root) 
        self.entry1.place(x=0, y=20)

        self.button = tk.Button(root, text="Clear", command=self.clear)
        self.button.place(x=125, y=20)
        # Creating Menubar
        menubar = tk.Menu(root)
        # Adding File Menu and commands
        file = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='File', menu=file)
        # file.add_command(label='Save', command=self.getter)
        file.add_separator()
        file.add_command(label='Exit', command=root.destroy)

        # Adding Edit Menu and commands
        edit = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Edit', menu=edit)
        # Changing brush types in nested menu
        nedit = tk.Menu(menubar, tearoff=0)
        edit.add_separator()
        edit.add_command(label='Clear', command=self.clear)
        # display Menu
        root.config(menu=menubar)

    def clear(self):
        # Created method for clearing all
        self.entry1.delete(0, END)


if __name__ == "__main__":
    root = tk.Tk()
    root.rowconfigure(1, weight=1)
    root.columnconfigure(0, weight=1)
    app = Drone(root)
    root.mainloop()
