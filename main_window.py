from tkinter import Tk, Button, Label, Entry
from random import choice

class MainWindow():

    def __init__(self):
        self.window = Tk(className='Laughing Fiesta')
        self.name_list = []

        self.name_collector = Entry(self.window)
        self.name_collector.pack()

        self.add_name_button = Button(self.window, text='Add name', command = self.collect_name)
        self.add_name_button.pack()

    def collect_name(self):
        new_name = self.name_collector.get()
        self.name_list.append(new_name)
        self.name_collector.delete(0)

    def select_name(self):
        chosen_name = choice(self.name_list)
        self.name_list.pop(chosen_name)
        label = Label(self.window, text=chosen_name)
        label.pack()

    def run(self):
        self.window.mainloop()


w = MainWindow()

w.run()