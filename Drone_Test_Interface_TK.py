
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox


class Grapher(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.offset = 0

    def create_widgets(self):
        # Create a canvas widget to graph the function
        self.canvas = tk.Canvas(self, width=500, height=500)
        self.canvas.grid(row=1, column=2, columnspan=3, sticky="nsew")

        # Initialize the canvas widget
        self.fig = plt.figure()
        self.canvas_agg = FigureCanvasTkAgg(self.fig, master=self.canvas)
        self.canvas_agg.draw()
        self.canvas_agg.get_tk_widget().pack()

        # Text entry for graph one
        self.func = tk.Entry(self)
        self.funclabel = tk.Label(self, text='Function 1')
        self.funclabel.grid(row=2, column=1, columnspan=1, sticky="ew")
        self.func.grid(row=3, column=1, columnspan=1, sticky="ew")

        self.min = tk.Entry(self)
        self.funclabel = tk.Label(self, text='Minimum')
        self.funclabel.grid(row=2, column=2, columnspan=1, sticky="ew")
        self.min.grid(row=3, column=2, columnspan=1, sticky="ew")

        self.max = tk.Entry(self)
        self.funclabel = tk.Label(self, text='Maximum')
        self.funclabel.grid(row=2, column=3, columnspan=1, sticky="ew")
        self.max.grid(row=3, column=3, columnspan=1, sticky="ew")

        self.point = tk.Entry(self)
        self.funclabel = tk.Label(self, text='Number of Points')
        self.funclabel.grid(row=2, column=4, columnspan=1, sticky="ew")
        self.point.grid(row=3, column=4, columnspan=1, sticky="ew")

        # Text entry for graph two
        self.func1 = tk.Entry(self)
        self.funclabel = tk.Label(self, text='Function 2')
        self.funclabel.grid(row=4, column=1, columnspan=1, sticky="ew")
        self.func1.grid(row=5, column=1, columnspan=1, sticky="ew")

        # Create a button to graph the function
        self.button = tk.Button(self, text="Graph", command=self.graph)
        self.button.grid(row=5, column=8, columnspan=5, sticky="ew")

        # Clear button
        self.button = tk.Button(self, text="Clear", command=self.clear)
        self.button.grid(row=4, column=8, columnspan=5, sticky="ew")

    def clear(self):
        # Created method for clearing all
        self.fig.clear()
        self.canvas_agg.draw()
        self.func.delete(0, 'end')
        self.func1.delete(0, 'end')
        self.min.delete(0, 'end')
        self.max.delete(0, 'end')
        self.point.delete(0, 'end')


    def graph(self):
        # Takes the info from inputted text
        sped = ('sin', 'cos', 'tan', 'log', 'sqrt')
        x = 0
        # Checks for x values if not to handle crash
        try:
            x_mn = self.min.get()
            x_mx = self.max.get()
            x_p = self.point.get()
            x = np.linspace(int(x_mn), int(x_mx), int(x_p))
        except (SyntaxError, NameError, ValueError):
            # Print error message and opens new window for error message
            print('Invalid Possible X-Axis Values')
            messagebox.showerror("Error Message", 'Invalid Possible X-Axis Values')
        # No crashes if something happens
        x_one = self.func.get()
        if x_one != "":
            try:
                # Uses loop to evaluate special cases
                x1_split = x_one.split('(')
                for i in x1_split:
                    if i in sped:
                        x_one = 'np.' + x_one
                y = eval(x_one)
                plt.plot(x, y, label=f'Graph {x_one}')
                plt.legend()
            except (SyntaxError, NameError):
                # Print error message and opens new window for error message
                print("Function Error: Try Reentering Function One")
                messagebox.showerror("Error Message", "Function Error: Try Reentering Function One")
        x_two = self.func1.get()
        if x_two != "":
            try:
                # Uses loop to evaluate special cases
                x_two_split = x_two.split('(')
                for i in x_two_split:
                    if i in sped:
                        x_two = 'np.' + x_two
                y2 = eval(x_two)
                plt.plot(x, y2, label=f'Graph {x_two}')
                plt.legend()
            except (SyntaxError, NameError):
                # Print error message and opens new window for error message
                print("Function Error: Try Reentering Function Two")
                messagebox.showerror("Error Message", "Function Error: Try Reentering Function Two")
        self.canvas_agg.draw()
        # Increment the offset
        self.offset += 1


if __name__ == '__main__':
    # Runner for graph maker
    grapher = tk.Tk()
    grapher.title("CNU_Desmos")
    app = Grapher(master=grapher)
    app.mainloop()
