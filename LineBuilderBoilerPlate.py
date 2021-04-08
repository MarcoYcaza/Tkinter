import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np


class LineBuilder:
    def __init__(self, line):
        self.line = line
        self.xs = list(line.get_xdata())
        self.ys = list(line.get_ydata())
        self.cid = line.figure.canvas.mpl_connect("button_press_event", self)

    def __call__(self, event):
        print("click", event)
        if event.inaxes != self.line.axes:
            return
        self.xs.append(event.xdata)
        self.ys.append(event.ydata)
        self.line.set_data(self.xs, self.ys)
        self.line.figure.canvas.draw()


# Definimos nuestra pantalla principal
root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Embeded Matplotlib Plot")

mu, sigma = 0, 0.1  # mean and standard deviation

data = np.random.normal(mu, sigma, 1000)
fig, ax = plt.subplots()


canvas = FigureCanvasTkAgg(fig, master=root)
(line,) = ax.plot([0], [0])  # empty line
linebuilder = LineBuilder(line)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        canvas.get_tk_widget().quit()
        print(linebuilder.ys)
        root.destroy()


root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
