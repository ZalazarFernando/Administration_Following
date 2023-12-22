import tkinter as tk
from tkinter import *

import Op_Follow

class Lists:
    selected_text_return = ""
    def __init__(self, app):
        self.app = app
        self.selected_item = None
        
        self.create_frame()
        self.show_info()

    def create_frame(self):
        self.this_frame = Frame(self.app)
        self.this_frame.config(bg = "#eb6434")
        self.this_frame.place(x=510,y=60 ,width=280,height=400)

    def refresh(self, filter_condition, selected_item=None, current_tab = None):
        self.lines_listbox.destroy()
        self.show_info(selected_item, current_tab, filter_condition)

    def set_lines_within_files(self, filter_condition, selected_item, current_tab = None):
        self.selected_category = selected_item
        self.selected_folder = current_tab

        if filter_condition == "" or filter_condition == None:
            return Op_Follow.get_info_element(
                        current_tab= current_tab,
                        selected_item= selected_item
                    )
        else:
            return Op_Follow.get_info_element(
                        current_tab= current_tab,
                        selected_item= selected_item,
                        filter_condition= filter_condition
                    )
    
    def show_info(self, selected_item = None, current_tab = None, filter_condition = None):
        if selected_item != None and current_tab != None:
            lines_within_files = self.set_lines_within_files(
                    filter_condition= filter_condition, 
                    selected_item= selected_item, 
                    current_tab= current_tab)

        self.lines_listbox = Listbox(self.this_frame)
        self.lines_listbox.pack(fill="both", expand=True)
        
        if selected_item != None and current_tab != None:
            for line in lines_within_files:
                    self.lines_listbox.insert(END, line)

        self.lines_listbox.bind("<<ListboxSelect>>", self.on_listbox_select)

    def on_listbox_select(self, event):
        file_listbox = event.widget #recupera el listbox que desencadenó el evento
        selected_index = file_listbox.curselection()

        if selected_index:
            self.selected_text_return = [self.lines_listbox.get(index) for index in selected_index]