import tkinter as tk
from tkinter import *
from tkinter import messagebox

from Adding_Category import Adding_Category
import Op_Follow

class Superior_Frame:

    def __init__(self, app, categories_frame):
        self.app = app
        self.categories_frame = categories_frame

        self.create_frame()
        self.create_btns()
        self.create_textbox_search()

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
        add_element = Adding_Category(self.app, self.categories_frame)

    def on_click_btn_delete(self):
        if messagebox.askokcancel("Warning", "Do you want to delete this item?") == True:
            Op_Follow.delete_category(
                folder=self.categories_frame.tab_text,
                name_category= self.categories_frame.selected_text_return[0]
            )

    def create_textbox_search(self):
        self.textbox_search = Entry(
            self.this_frame, 
            textvariable=self.categories_frame.filter_condition
            )
        self.textbox_search.pack(fill="both", side=RIGHT) 

        self.categories_frame.filter_condition.trace_add("write", self.on_search_change)

    def on_search_change(self, *args):
        self.categories_frame.set_search_condition(self.categories_frame.filter_condition.get())