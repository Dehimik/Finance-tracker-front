import tkinter as tk

from app.assets.styles.styles import default_styles

class ProfileEdit(tk.Frame):
    def __init__(self, master, user_id):
        super().__init__(master)
        self.pack()
        self.create_widgets(user_id)
        default_styles(self)

    def creare_widgets(self, user_id):
        tk.Label(text="Edit name")