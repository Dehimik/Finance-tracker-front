import tkinter as tk
from tkinter import messagebox
import requests

from app.services.api_client import register_request

class RegisterWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.create_widgets()
    def create_widgets(self):
        tk.Label(self, text="Email").pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack()

        tk.Label(self, text="Nickname").pack()
        self.nickname_entry = tk.Entry(self)
        self.nickname_entry.pack()

        tk.Label(self, text="Password").pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        tk.Label(self, text="Retype password").pack()
        self.confirm_password_entry = tk.Entry(self, show="*")
        self.confirm_password_entry.pack()
        tk.Button(self, text="Register", command=self.register).pack()

    def register(self):
        email = self.email_entry.get()
        nickname = self.nickname_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if not email or not nickname or not password or not confirm_password:
            messagebox.showwarning("Error", "Fill all fields!")
            return
        if password != confirm_password:
            messagebox.showerror("Error", "Passwords doesnt match!")
            return
        try:
            response = register_request(email, nickname, password)

            if "message" in response:
                messagebox.showinfo("Success", "Register success! Login now.")
            else:
                messagebox.showerror("Error", "Email already exists!")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Registration unsuccessfully: {e}")