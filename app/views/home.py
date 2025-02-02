import tkinter as tk

class HomeWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.create_widgets()
    def create_widgets(self):
        tk.Button(self, text = "Profile", command = self.open_profile).pack()


    def open_profile(self):
        pass