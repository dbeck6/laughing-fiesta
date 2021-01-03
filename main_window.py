from tkinter import Tk, Button, Label, Entry
from random import choice

class MainWindow():

    def __init__(self):
        self.window = Tk(className='Laughing Fiesta')
        self.window.geometry("300x200")
        
        self.name_list = []

        self.name_collector = Entry(self.window)
        self.name_collector.pack()

        self.add_name_button = Button(self.window, text='Add name', command=self.collect_name)
        self.add_name_button.pack()

        self.choose_name_button = Button(self.window, text='Pick name', command=self.select_name)
        self.choose_name_button.pack()

    def collect_name(self):
        new_name = self.name_collector.get()
        self.name_list.append(new_name)
        name_length = len(new_name)
        self.name_collector.delete(0, name_length)

    def select_name(self):
        if len(self.name_list) > 0:
            chosen_name = choice(self.name_list)
            if len(chosen_name) > 0:
                self.name_list.remove(chosen_name)
                label = Label(self.window, text=chosen_name)
                label.pack()

    def run(self):
        self.window.mainloop()
