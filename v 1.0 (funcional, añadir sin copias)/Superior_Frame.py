import tkinter as tk
from tkinter import *
from tkinter import ttk

from Adding_Category import Adding_Category

class Superior_Frame:

    def __init__(self, app, categories_frame):
        self.app = app
        self.categories_frame = categories_frame

        self.create_frame()
        self.create_btns()

    def create_frame(self):
        self.this_frame = tk.Frame(self.app)
        self.this_frame.config(bg = "#ec03fc")
        self.this_frame.place(x=0,y=0 ,width=800,height=30)

    def create_btns(self):
        self.create_btn_add()

    def create_btn_add(self):
        self.btn_add = tk.Button(self.this_frame, text="Add", command=self.on_click_btn_add)
        self.btn_add.pack(fill="both", side=LEFT)
        self.btn_add.config(width=10, height=30)

    def on_click_btn_add(self):
        self.app.withdraw()
        adding_app = Adding_Category(self.app, self.categories_frame)
