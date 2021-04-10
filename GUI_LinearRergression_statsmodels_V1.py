from tkinter import *
import tkinter.font as tkFont
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm


class LineBuilder:
    def __init__(self, line):
        self.line = line
        self.xs = list(line.get_xdata())
        self.ys = list(line.get_ydata())
        self.cid = line.figure.canvas.mpl_connect("button_press_event", self)

    def __call__(self, event):
        if event.inaxes != self.line.axes:
            return
        self.xs.append(event.xdata)
        self.ys.append(event.ydata)
        self.line.set_data(self.xs, self.ys)
        self.line.figure.canvas.draw()


# Definimos nuestra pantalla principal
root = tk.Tk()
root.geometry("900x800")
root.resizable(True, True)
fontStyle = tkFont.Font(family="Consolas", size=10)
root.title("Regression Interface")


def initializeLineGraph(ax):
    (line,) = ax.plot([0], [0])  # empty line
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)

    # linebuilder =
    return LineBuilder(line)


def drawRegression(event=None):

    ax.scatter(linebuilder.xs, linebuilder.ys, marker="+", c="b", s=30)

    model = LinearRegression()

    x = np.array(linebuilder.xs).reshape(-1, 1)
    y = np.array(linebuilder.ys).reshape(-1, 1)
    reg = model.fit(x, y)

    ax.plot(x, reg.predict(x), marker="+", c="r")

    x = sm.add_constant(x)
    results = sm.OLS(y, x).fit()

    summaryText.set(results.summary())

    label = tk.Label(
        root,
        text=summaryText.get(),
        relief=RIDGE,
        font=fontStyle,
        justify=CENTER,
    )
    label.grid(row=3, columnspan=4, padx=(10, 10), pady=(10, 10))

    canvas.draw()


fig = Figure(figsize=(8, 3), dpi=100)
ax = fig.add_subplot(111)


# -------- Create Some Variables
summaryText = tk.StringVar()
summaryText.set("log")

# -------- Define Canvas Buttons and LabelViews
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
button1 = tk.Button(root, text="Regression", command=drawRegression, font=fontStyle)
button2 = tk.Button(root, text="Other", command=drawRegression, font=fontStyle)
button3 = tk.Button(root, text="Other", command=drawRegression, font=fontStyle)


# --------  Define our linebuilder
linebuilder = initializeLineGraph(ax)

# -------- Placing Elements
button1.grid(row=0, column=0, padx=(10, 10), pady=(10, 10))
# button2.grid(row=0, column=1, padx=(10, 10), pady=(10, 10))
# button3.grid(row=0, column=2, padx=(10, 10), pady=(10, 10))
canvas_widget.grid(row=1, columnspan=4, column=0, padx=(10, 10), pady=(10, 10))


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        canvas.get_tk_widget().quit()
        root.destroy()


root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
