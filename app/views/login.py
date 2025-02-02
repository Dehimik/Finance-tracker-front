import tkinter as tk
from tkinter import messagebox
import requests

from app.services.api_client import login_request

class LoginWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Nickname").pack()
        self.nickname_entry = tk.Entry(self)
        self.nickname_entry.pack()

        tk.Label(self, text="Password").pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        tk.Button(self, text="Login", command=self.login).pack()
        tk.Button(self, text="Registration", command=self.go_to_register).pack()

    def login(self):
        nickname = self.nickname_entry.get()
        password = self.password_entry.get()

        if not nickname or not password:
            messagebox.showwarning("Error", "Fill all fields!")
            return

        try:
            response = login_request(nickname, password)

            if "message" in response:
                messagebox.showinfo("Success", "Login successfully!")
                self.master.nickname = nickname
                self.master.show_home()
            else:
                messagebox.showerror("Error", "Incorrect nickname or password!")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Shit happens: {e}")

    def go_to_register(self):
        self.master.show_register()