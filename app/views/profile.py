import tkinter as tk

from app.services.api_client import get_user
from app.services.api_client import update_account
from app.services.api_client import delete_account
from app.services.api_client import logout

class ProfileWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.create_widgets()