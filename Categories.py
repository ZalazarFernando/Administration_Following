import tkinter as tk
from tkinter import *
from tkinter import ttk
import os

from Superior_Frame import Superior_Frame
import Op_Follow

class Categories:
    tab_listbox_mapping = {}
    search_condition = ""

    def __init__(self, app, lists_frame):
        self.app = app
        self.lists_frame = lists_frame
        self.filter_condition = tk.StringVar(app)

        self.create_frame(app)

        #self.sup_frame = Superior_Frame(self.this_frame)
        self.tab_control = ttk.Notebook(self.this_frame)

        self.tab_control.pack(expand=1, fill="both")

        self.add_tabs_with_file_list("apps/Instagram")
        self.add_tabs_with_file_list("apps/Youtube")

        self.this_frame.bind("<FocusIn>", lambda event: self.refresh())

    def create_frame(self,app):
        self.this_frame = Frame(app)
        self.this_frame.config(bg="#03fc88")
        self.this_frame.place(x=0,y=30 ,width=500,height=500)

    def refresh(self):
        for tab in self.tab_control.tabs():
            self.tab_control.forget(tab)

        self.add_tabs_with_file_list("apps/Instagram")
        self.add_tabs_with_file_list("apps/Youtube")

    def add_tabs_with_file_list(self, directory):
        directory_name = directory.replace("apps/", "")
        file_list = Op_Follow.get_info_category(directory)

        tab = ttk.Frame(self.tab_control)
        self.tab_control.add(tab, text=directory_name)

        file_listbox = Listbox(tab)
        file_listbox.pack(fill="both", expand=True)

        for file in file_list:
            name, extension = os.path.splitext(file)
            file_listbox.insert(END, name)

        #diccionario que guarda la relación de en qué pestaña está la listbox
        self.tab_listbox_mapping[file_listbox] = tab 

        file_listbox.bind("<<ListboxSelect>>", self.on_listbox_select)

    def set_search_condition(self, text):
        self.search_condition = text

    def on_listbox_select(self, event):
        file_listbox = event.widget #recupera el listbox que desencadenó el evento
        selected_index = file_listbox.curselection()

        if selected_index:
            selected_item = file_listbox.get(selected_index[0])
            self.selected_text_return = [file_listbox.get(index) for index in selected_index]

            current_tab = self.tab_listbox_mapping.get(file_listbox)
            #obtiene el atributo text o sea el nombre
            self.tab_text = self.tab_control.tab(current_tab, "text")

            if current_tab:
                if self.filter_condition == None:
                    self.lists_frame.refresh(
                        selected_item= selected_item, 
                        current_tab= self.tab_text)
                else:
                    self.lists_frame.refresh(
                        filter_condition= self.search_condition, 
                        selected_item= selected_item, 
                        current_tab= self.tab_text)
