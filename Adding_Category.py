import tkinter as tk
from tkinter import *
from tkinter import ttk

import Op_Follow

class Adding_Category(tk.Tk):

    def __init__(self, app, categories_frame):
        super().__init__()

        self.app = app
        self.categories_frame = categories_frame

        self.geometry("300x190")
        self.title("Add category")
        self.resizable(0,0)

        self.create_widget()

        self.protocol("WM_DELETE_WINDOW", self.close_this_app)

    def create_widget(self):
        self.create_frame()
        self.create_textbox_category()
        self.create_textbox_app()
        self.create_button_done()

    def create_frame(self):
        self.this_frame = Frame(self)
        self.this_frame.config(bg = "#ec03fc")
        self.this_frame.place(x=0, y=0, width=300, height=190)

    def create_textbox_category(self):
        label_category = Label(self.this_frame, text="what category:")
        label_category.place(x=10, y=30, width=280, height=20)

        self.textbox_category = Entry(self.this_frame)
        self.textbox_category.place(x=10, y=50, width=280, height=20)

    def create_textbox_app(self):
        label_app = Label(self.this_frame, text="what app:")
        label_app.place(x=10, y=70, width=280, height=20)

        options = Op_Follow.get_app_available()

        self.combo_apps = ttk.Combobox(self.this_frame, values=options)
        self.combo_apps.place(x=10, y=90, width=280, height=20)

    def create_button_done(self):
        self.btn_done = Button(self.this_frame, text="Done", command=self.save_follow)
        self.btn_done.place(x=200, y=130, width=50, height=30)

    def save_follow(self):
        Op_Follow.save_category(
            folder= self.combo_apps.get(),
            name_new_category= self.textbox_category.get()
        )

        self.close_this_app()

    def close_this_app(self):
        self.categories_frame.refresh()
        self.app.deiconify()
        self.destroy()