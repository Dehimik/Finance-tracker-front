import tkinter as tk
import requests
from tkinter import messagebox

from app.services.api_client import update_account
from app.assets.styles.styles import default_styles

class ProfileEdit(tk.Frame):
    def __init__(self, master, user_id):
        super().__init__(master)
        self.pack()
        self.create_widgets(user_id)
        default_styles(self)

    def create_widgets(self, user_id):
        tk.Label(self, text=f"{user_id}").pack()
        tk.Label(self, text="Edit name").pack()
        self.user_name_entry = tk.Entry(self)
        self.user_name_entry.pack()

        tk.Label(self, text="Edit email").pack()
        self.user_email_entry = tk.Entry(self)
        self.user_email_entry.pack()

        tk.Label(self, text="Edit password").pack()
        self.user_password_entry = tk.Entry(self)
        self.user_password_entry.pack()

        tk.Label(self, text="Edit currency").pack()
        self.user_currency_entry = tk.Entry(self)
        self.user_currency_entry.pack()

        tk.Button(self, text="Edit", command=lambda: self.edit_profile(user_id)).pack()

    def edit_profile(self, user_id):
        user_name = self.user_name_entry.get()
        user_email = self.user_email_entry.get()
        user_password = self.user_password_entry.get()
        user_currency = self.user_currency_entry.get()

        try:
            response = update_account(user_id, user_name, user_email, user_password, user_currency)
            if response.get("status") == 200:
                messagebox.showinfo("Success!", "Profile has been successfully updated!")
                self.open_profile()
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Shit happens: {e}")

    def open_profile(self):
        self.master.show_profile()