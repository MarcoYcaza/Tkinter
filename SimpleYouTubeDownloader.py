import tkinter as tk
from tkinter import filedialog
from pytube import YouTube
from tkinter import ttk


def UploadAction(event=None):
    try:
        if file_type.get():
            ytURL = YouTube(file_text.get())

            ytURL.streams.filter(progressive=True, file_extension="mp4").order_by(
                "resolution"
            ).desc().first().download()
        else:
            ytURL = YouTube(file_text.get())
            ytURL.streams.filter(type="audio").order_by(
                "mime_type"
            ).desc().first().download()

        log_text.set("La descarga ha empezado")
        name_label1 = ttk.Label(log_frame, text=log_text.get())
        name_label1.grid(row=0, column=1, pady=(10, 10))
    except:
        log_text.set("Hubo un error con la URL")
        name_label1 = ttk.Label(log_frame, text=log_text.get())
        name_label1.grid(row=0, column=1, padx=(0, 10))


root = tk.Tk()
root.title("Descargar Video Youtube")
root.geometry("500x120")

root.columnconfigure(1, weight=1)
root.rowconfigure(1, weight=1)

file_text = tk.StringVar()
log_text = tk.StringVar()
log_text.set("Salida ...")

file_type = tk.BooleanVar()
file_type.set(True)

# -------------------------------------------------------------------

name_label = ttk.Label(root, text="Url :")
name_label.grid(row=0, column=0, padx=(0, 10))

myURL = ttk.Entry(root, textvariable=file_text)
myURL.insert(0, "pega el enlace de la url...")
myURL.grid(row=0, column=1, pady=(10, 10), sticky="EW")
myURL.focus()

button = ttk.Button(root, text="Descargar", command=UploadAction)
button.grid(row=0, column=2, padx=(10, 10))

# -------------------------------------------------------------------

log_frame = ttk.Frame(root, padding=(20, 10))
log_frame.columnconfigure(1, weight=1)
log_frame.grid(column=1)

radio_video = tk.Radiobutton(
    log_frame, text="video", padx=20, variable=file_type, value=True
)


radio_audio = tk.Radiobutton(
    log_frame, text="audio", padx=20, variable=file_type, value=False
)

radio_video.grid(row=1, column=1, padx=(0, 10))
radio_audio.grid(row=1, column=0, padx=(0, 10))


root.mainloop()
