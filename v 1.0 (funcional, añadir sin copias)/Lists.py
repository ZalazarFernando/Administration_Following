import tkinter as tk
from tkinter import *
from tkinter import ttk

class Lists:

    def __init__(self, app):
        self.app = app
        
        self.create_frame()
        self.show_info()

    def create_frame(self):
        self.this_frame = Frame(self.app)
        self.this_frame.config(bg = "#eb6434")
        self.this_frame.place(x=510,y=30 ,width=280,height=500)

    def refresh_this_frame(self, selected_item=None, current_tab = None):
        self.lines_listbox.destroy()
        self.show_info(selected_item, current_tab)

    def set_lines_within_files(self, selected_item, current_tab = None):
        lines_within_files = ()
        try:
            with open(current_tab+"/"+selected_item+".txt", 'r') as file_read:
                lines_within_files = file_read.readlines()
        finally:
            return lines_within_files
    
    def show_info(self, selected_item=None, current_tab = None):
        lines_within_files = self.set_lines_within_files(selected_item, current_tab)

        self.lines_listbox = Listbox(self.this_frame)
        self.lines_listbox.pack(fill="both", expand=True)

        for line in lines_within_files:
            self.lines_listbox.insert(END, line)