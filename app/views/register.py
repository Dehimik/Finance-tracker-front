import tkinter as tk
from tkinter import messagebox
import requests

from app.services.api_client import register_request
from app.assets.styles.styles import default_styles

class RegisterWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        default_styles(self)

    def create_widgets(self):
        tk.Label(self, text="Email").pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack()

        tk.Label(self, text="Username").pack()
        self.user_name_entry = tk.Entry(self)
        self.user_name_entry.pack()

        tk.Label(self, text="Password").pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        tk.Label(self, text="Retype password").pack()
        self.confirm_password_entry = tk.Entry(self, show="*")
        self.confirm_password_entry.pack()
        tk.Button(self, text="Register", command=self.register).pack()
        tk.Button(self, text="Login", command=self.go_to_login).pack()

    def register(self):
        email = self.email_entry.get()
        user_name = self.user_name_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if not email or not user_name or not password or not confirm_password:
            messagebox.showwarning("Error", "Fill all fields!")
            return
        if password != confirm_password:
            messagebox.showerror("Error", "Passwords doesnt match!")
            return
        try:
            response = register_request(email, user_name, password)

            if "id" in response:
                messagebox.showinfo("Success", "Register success! Login now.")
            else:
                messagebox.showerror("Error", "Email already exists!")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Registration unsuccessfully: {e}")\

    def go_to_login(self):
        self.master.show_login()