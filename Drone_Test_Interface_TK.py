import tkinter as tk
from tkinter import colorchooser
from PIL import ImageGrab
import os
from tkinter import *
from tkinter import filedialog


class Paint:
    def __init__(self, root):
        self.image = os.path.join('data', 'Kw.png')
        self.root = root
        self.root.title("DRONE")
        self.root.title("DRONE API")
        self.root.geometry("800x600")
        self.canvas = tk.Canvas(self.root, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=5, sticky="nsew")
        self.create_widgets()

    def colors(self):
        # Color pallet
        color_num = colorchooser.askcolor(title="Color Options")
        self.pen_color = color_num[1]

    def create_widgets(self):
        # Pen size
        current_value = tk.DoubleVar()
        self.funclabel = tk.Label(root, text='Brush Size:')
        self.funclabel.place(x=0, y=0)
        self.slider = tk.Scale(root, from_=0, to=100, length=650, orient='vertical', variable=current_value)
        self.slider.place(x=0, y=20)

        # Creating Menubar
        menubar = tk.Menu(root)
        # Adding File Menu and commands
        file = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='File', menu=file)
        file.add_command(label='Save', command=self.getter)
        file.add_separator()
        file.add_command(label='Exit', command=root.destroy)
        file.add_command(label='How I Felt About This Lab', command=self.show_image)

        # Adding Edit Menu and commands
        edit = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Edit', menu=edit)
        # Changing brush types in nested menu
        nedit = tk.Menu(menubar, tearoff=0)
        edit.add_cascade(label='Brush Options', menu=nedit)
        nedit.add_command(label='Square', command=self.change_square)
        nedit.add_command(label='Circle', command=self.change_circle)
        nedit.add_command(label='Triangle', command=self.change_poly)
        # Changing colors
        edit.add_command(label='Color Options', command=self.colors)
        edit.add_separator()
        edit.add_command(label='Clear', command=self.clear)
        # display Menu
        root.config(menu=menubar)

    # Saving images to png
    def getter(self):
        x = self.root.winfo_rootx() + self.canvas.winfo_x()
        y = self.root.winfo_rooty() + self.canvas.winfo_y()
        x1 = x + self.canvas.winfo_width()
        y1 = y + self.canvas.winfo_height()
        filename = tk.filedialog.asksaveasfilename()
        fileloc = os.path.join('data', f'Image {self.filenum}.png')
        ImageGrab.grab().crop((x + 65, y + 21, x1, y1 - 5)).save(fileloc)
        self.filenum += 1

    # Hidden changes
    def show_image(self):
        gif1 = PhotoImage(file=self.image)
        self.canvas.create_image(400, 300, image=gif1)
        self.canvas.gif1 = gif1

    # Methods used for handling commands
    def change_square(self):
        self.pen_shape = 'square'

    def change_circle(self):
        self.pen_shape = 'circle'

    def change_poly(self):
        self.pen_shape = 'poly'

    def clear(self):
        self.canvas.delete('all')


if __name__ == "__main__":
    root = tk.Tk()
    root.rowconfigure(1, weight=1)
    root.columnconfigure(0, weight=1)
    app = Paint(root)
    root.mainloop()
