import tkinter as tk
from tkinter import ttk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np

#Definimos nuestra pantalla principal
root = tk.Tk()
root.geometry("600x400")
root.resizable(False,False)
root.title("Embeded Matplotlib Plot")

mu, sigma = 0, 0.1 # mean and standard deviation

data = np.random.normal(mu, sigma, 1000)

fig =  Figure(figsize=(5,4),dpi=100)
myPlot =  fig.add_subplot(111)

canvas = FigureCanvasTkAgg(fig,master=root)

def comando_actualizar_grafico(event):
    #Va a crear y actualizar algún gráfico segun como movamos una perilla
    myPlot.cla()
    bins = scale.get()
    myPlot.hist(data,bins=int(bins))

    myPlot.set_title(bins)

    canvas.draw()

scale = ttk.Scale(root,orient="horizontal",from_=30,to=100,command=comando_actualizar_grafico)
scale.set(45)
scale.pack(fill="x")


canvas.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH,expand=1)

canvas.draw()

root.mainloop()
