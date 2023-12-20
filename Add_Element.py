import tkinter as tk
from tkinter import *
from tkinter import ttk

import Op_Follow


class Add_Element(tk.Tk):

    def __init__(self, app):
        super().__init__()

        self.app = app

        self.geometry("300x220")
        self.title("Add follow")
        self.resizable(0,0)

        self.create_widget()

        self.protocol("WM_DELETE_WINDOW", self.close_this_app)

    def create_widget(self):
        self.create_frame()
        self.create_textbox_name()
        self.create_textbox_category()
        self.create_textbox_app()
        self.create_textbox_specification()
        self.create_button_done()

    def create_frame(self):
        self.this_frame = tk.Frame(self)
        self.this_frame.config(bg = "#ec03fc")
        self.this_frame.place(x=0,y=0 ,width=300,height=300)

    def create_textbox_name(self):
        label_name = Label(self.this_frame, text="Name of follow:")
        label_name.place(x=10, y=10, width=280, height=20)

        self.textbox_name = Entry(self.this_frame)
        self.textbox_name.place(x=10, y=30, width=280, height=20)

    def create_textbox_specification(self):
        label_specification = Label(self.this_frame, text="Specification:")
        label_specification.place(x=10, y=50, width=280, height=20)

        self.textbox_specification = Entry(self.this_frame)
        self.textbox_specification.place(x=10, y=70, width=280, height=20)

    def create_textbox_category(self):
        label_category = Label(self.this_frame, text="what category:")
        label_category.place(x=10, y=90, width=280, height=20)

        options = []#cambiar para que busque cuantas y qué categorías hay

        self.combo_categories = ttk.Combobox(self.this_frame, values=options)
        self.combo_categories.place(x=10, y=110, width=280, height=20)
        self.combo_categories["state"] = "disabled"
        """self.textbox_category = Entry(self.this_frame)
        self.textbox_category.place(x=10, y=110, width=280, height=20)"""

    def create_textbox_app(self):
        label_app = Label(self.this_frame, text="what app:")
        label_app.place(x=10, y=130, width=280, height=20)

        options = Op_Follow.get_app_available()

        self.combo_apps = ttk.Combobox(self.this_frame, values=options)
        self.combo_apps.place(x=10, y=150, width=280, height=20)
        self.combo_apps.bind("<<ComboboxSelected>>", self.on_select_first)

        """self.textbox_app = Entry(self.this_frame)
        self.textbox_app.place(x=10, y=150, width=280, height=20)"""

    def on_select_first(self, event):
        self.combo_categories.configure(state="normal")
        name_folder = self.combo_apps.get()
        aux_str = Op_Follow.get_categories_available(name_folder)
        options = []
        for aux in aux_str:
            options.append(aux.replace(".txt", ""))

        self.combo_categories["values"] = options

    def create_button_done(self):
        self.btn_done = Button(self.this_frame, text="Done", command=self.save_follow)
        self.btn_done.place(x=200, y=180, width=50, height=30)

    def save_follow(self):
        if (Op_Follow.compare_with_file(
            folder=self.textbox_app.get(),
            category=self.textbox_category.get(),
            name=self.textbox_name.get()
        ) == 0):
            Op_Follow.save_element(
                folder=self.textbox_app.get(),
                category=self.textbox_category.get(),
                name=self.textbox_name.get(),
                specification=self.textbox_specification.get()
            )

            self.close_this_app()

    def close_this_app(self):
        #self.categories_frame.refresh()
        self.app.deiconify()
        self.destroy()