import tkinter as tk
from tkinter import *
from tkinter import ttk

from Menu_Lists import Menu_lists

class Lists:

    def __init__(self, app):
        self.app = app
        self.selected_item = None
        
        self.create_frame_up()
        self.create_frame_down()
        self.show_info()

        self.Menu = Menu_lists(self.frame_up, self.app, self.selected_folder, self.selected_category, self.selected_item)
    
    def create_frame_up(self):
        self.frame_up = Frame(self.app)
        self.frame_up.config(bg = "#eb6434")
        self.frame_up.place(x=510,y=30 ,width=280,height=30)

    def create_frame_down(self):
        self.frame_down = Frame(self.app)
        self.frame_down.config(bg = "#eb6434")
        self.frame_down.place(x=510,y=60 ,width=280,height=400)

    def refresh_frame_down(self, selected_item=None, current_tab = None):
        self.lines_listbox.destroy()
        self.show_info(selected_item, current_tab)
        self.Menu = Menu_lists(self.frame_up, self.selected_folder, self.selected_category, self.selected_item)
        

    def set_lines_within_files(self, selected_item, current_tab = None):
        self.selected_category = selected_item
        self.selected_folder = current_tab
        lines_within_files = ()
        try:
            with open(current_tab+"/"+selected_item+".txt", 'r') as file_read:
                lines_within_files = file_read.readlines()
        finally:
            return lines_within_files
    
    def show_info(self, selected_item=None, current_tab = None):
        lines_within_files = self.set_lines_within_files(selected_item, current_tab)

        self.lines_listbox = Listbox(self.frame_down)
        self.lines_listbox.pack(fill="both", expand=True)

        self.lines_listbox.bind("<<ListboxSelect>>", self.on_listbox_select)

        for line in lines_within_files:
            self.lines_listbox.insert(END, line)

    def on_listbox_select(self, event):
        file_listbox = event.widget #recupera el listbox que desencadenó el evento
        selected_index = file_listbox.curselection()

        print(file_listbox.get(selected_index[0]))

        if selected_index:
            self.Menu.destroy_frame
            self.selected_item = file_listbox.get(selected_index[0])
            self.Menu = Menu_lists(self.frame_up, self.selected_folder, self.selected_category, self.selected_item)