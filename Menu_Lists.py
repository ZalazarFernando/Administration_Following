import tkinter as tk
from tkinter import *
from tkinter import ttk

import Op_Follow
from Add_Element import Add_Element

class Menu_lists:

    def __init__(self, frame, app, selected_folder, selected_category, selected_item = None):
        self.app = app
        self.frame = frame
        self.folder = selected_folder
        self.category = selected_category
        self.name = selected_item

        self.create_frame()
        self.create_btns()

    def create_frame(self):
        self.this_frame = tk.Frame(self.frame)
        self.this_frame.config(bg = "#ec03fc")
        self.this_frame.place(x=0,y=0 ,width=800,height=30)

    def destroy_frame(self):
        self.this_frame.destroy()

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
        add_element = Add_Element(self.app)

    def on_click_btn_delete(self):
        Op_Follow.delete_name(
            self.folder,
            self.category,
            self.name
        )