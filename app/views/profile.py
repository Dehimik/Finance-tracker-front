import tkinter as tk

from app.services.api_client import get_user
from app.services.api_client import update_account
from app.services.api_client import delete_account

class ProfileWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Email").pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack()

        tk.Button(self, text="Logout", command=self.logout).pack()

    def logout(self):
        self.master.show_login()