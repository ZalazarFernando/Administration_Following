import tkinter as tk
from tkinter import *
from tkinter import ttk

import Op_Follow

class Menu_lists:

    def __init__(self, app, selected_folder,selected_category, selected_item = None):
        self.app = app

        self.folder = selected_folder
        self.category = selected_category
        self.name = selected_item

        self.create_frame()
        self.create_btns()

    def create_frame(self):
        self.this_frame = tk.Frame(self.app)
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
        pass
        #codificar una manera para que se agreguen los nombres al archivo
        #sin necesidad de poner a que categoría pertenece (porque ya se está dentro de la categoría misma)

    def on_click_btn_delete(self):
        Op_Follow.delete_name(
            self.folder,
            self.category,
            self.name
        )