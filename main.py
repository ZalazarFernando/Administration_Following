import tkinter as tk
from tkinter import*

from Categories import Categories
from Lists import Lists
from Superior_Frame import Superior_Frame

app  = tk.Tk()
app.geometry("800x500")
app.title("Organización seguidos")
app.resizable(0,0)

lists_frame = Lists(app)

categories_frame = Categories(app, lists_frame)

superior_frame = Superior_Frame(app, categories_frame)

app.mainloop()