import tkinter as tk

from app.services.api_client import create_transaction
from app.services.api_client import get_transactions
from app.services.api_client import update_transaction
from app.services.api_client import delete_transaction

class HomeWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.create_widgets()
    def create_widgets(self):
        tk.Button(self, text = "Profile", command = self.open_profile).pack()


    def open_profile(self):
        pass