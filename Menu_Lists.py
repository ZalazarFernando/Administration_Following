import tkinter as tk
from tkinter import *
from tkinter import ttk

import Op_Follow
from Add_Element import Add_Element

class Menu_lists:

    def __init__(self, app, lists):
        self.app = app
        self.folder = lists.selected_folder
        self.category = lists.selected_category
        self.name = lists.selected_item

        self.create_frame()
        self.create_btns()

    def create_frame(self):
        self.frame = tk.Frame(self.app)
        self.frame.config(bg = "#eb6434")
        self.frame.place(x=510,y=30 ,width=280,height=30)

    """def destroy_frame(self):
        self.this_frame.destroy()"""

    def create_btns(self):
        self.create_btn_add()
        self.create_btn_delete()
        
    def create_btn_add(self):
        self.btn_add = tk.Button(self.frame, text="Add", command=self.on_click_btn_add)
        self.btn_add.pack(fill="both", side=LEFT)
        self.btn_add.config(width=10, height=30)

    def create_btn_delete(self):
        self.btn_delete = tk.Button(self.frame, text="Delete", command=self.on_click_btn_delete)
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