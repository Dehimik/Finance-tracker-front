import tkinter as tk

from app.services.api_client import get_user
from app.assets.formats.dateformats import format_date_dbY
from app.assets.styles.styles import default_styles

class ProfileWindow(tk.Frame):
    def __init__(self, master, user_id):
        super().__init__(master)
        self.pack()
        self.create_widgets(user_id)
        default_styles(self)

    def create_widgets(self, user_id):
        user = get_user(user_id)
        username = user.get("data", {}).get("user_name")
        email = user.get("data", {}).get("email")
        created_at = format_date_dbY(user.get("data", {}).get("created_at"))
        currency = user.get("data", {}).get("currency")
        tk.Label(self, text=f"Username: {username}").pack()
        tk.Label(self, text=f"Email: {email}").pack()
        tk.Label(self, text=f"User currency: {currency}").pack()
        tk.Label(self, text=f"Created at: {created_at}").pack()

        tk.Button(self, text="Edit profile", command=self.open_edit_profile).pack()
        tk.Button(self, text="Back to home", command=self.open_home).pack()
        tk.Button(self, text="Logout", command=self.logout).pack()

    def logout(self):
        self.master.show_login()

    def open_home(self):
        self.master.show_home()

    def open_edit_profile(self):
        self.master.show_edit_profile()