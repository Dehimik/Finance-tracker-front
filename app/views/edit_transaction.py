import tkinter as tk

from app.assets.styles.styles import default_styles

class TransactionEdit(tk.Frame):
    def __init__(self, master, transaction_id):
        super().__init__(master)
        self.pack()
        self.create_widgets(transaction_id)
        default_styles(self)

    def create_widgets(self, transaction_id):
        tk.Label()