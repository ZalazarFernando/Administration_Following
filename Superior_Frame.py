import tkinter as tk
from tkinter import *
from tkinter import ttk

from Adding_App import Adding_app

class Superior_Frame:

    def __init__(self, app, categories_frame=None):
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
        self.create_btn_delete()
        
    def create_btn_add(self):
        self.btn_add = tk.Button(self.this_frame, text="Add", command=self.on_click_btn_add)
        self.btn_add.pack(fill="both", side=LEFT)
        self.btn_add.config(width=10, height=30)

    def create_btn_delete(self):
        self.btn_delete = tk.Button(self.this_frame, text="Delete", command=self.on_click_btn_delete)
        self.btn_delete.pack(fill="both", side=LEFT)
        self.btn_delete.config(width=10, height=30)

    def on_click_btn_add(self):
        self.app.withdraw()
        adding_app = Adding_app(self.app, self.categories_frame)

    def on_click_btn_delete(self):
        pass
