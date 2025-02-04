import re
import tkinter as tk
from tkinter import messagebox

from app.services.api_client import create_transaction
from app.services.api_client import get_transactions
from app.services.api_client import update_transaction
from app.services.api_client import delete_transaction
from app.assets.formats.dateformats import format_date_timeWithHMp
from app.assets.styles.styles import default_styles

class HomeWindow(tk.Frame):
    def __init__(self, master, user_id):
        super().__init__(master)
        self.pack()
        self.create_widgets(user_id)
        default_styles(self)
    def create_widgets(self, user_id):
        tk.Button(self, text = "Profile", command = self.open_profile).pack()
        tk.Label(self, text="BALANCE HERE").pack()
        tk.Button(self, text="New transaction").pack()

        self.canvas = tk.Canvas(self, bg="#f5f5f5")
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="#f5f5f5")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.window = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw", width=self.canvas.winfo_width())

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="right", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        transactions = get_transactions(user_id).get("data", {}).get("transactions",[])

        if self.count_transactions(user_id) > 0:
            for transaction in transactions:
             self.create_transaction_card(self.scrollable_frame, transaction)
        else:
            messagebox.showerror("Error", "This user doesnt have any transactions!")

        self.bind("<Configure>", self.update_canvas_width)

    def update_canvas_width(self, event=None):
        self.canvas.itemconfig(self.window, width=self.winfo_width())

    def open_profile(self):
        self.master.show_profile()

    def create_transaction_card(self, parent, transaction):
        if not isinstance(transaction, dict):
            messagebox.showerror("Error: transaction is not dict!", transaction)
            return
        # Take info from transaction
        category = transaction.get("category")
        description = transaction.get("description")
        created_at = format_date_timeWithHMp(transaction.get("created_at"))
        amount = transaction.get("amount")

        # Create cool card here
        card = tk.Frame(parent, bg="#e0e3cf", padx=10, pady=10, width=196, height=48)
        card.pack(fill="x", padx=15, pady=15)

        # Top: Name+amount
        top_frame = tk.Frame(card, bg="#e0e3cf")
        top_frame.pack(fill="x")

        tk.Label(top_frame, text=f"{description}", font=("Arial", 14, "bold"), bg="#e0e3cf").pack(side="left")
        tk.Label(top_frame, text=f"{amount}", font=("Arial", 14, "bold"), fg="#004225", bg="#e0e3cf").pack(
            side="right")

        # Bottom: Category+time
        bottom_frame = tk.Frame(card, bg="#e0e3cf")
        bottom_frame.pack(fill="x")

        tk.Label(bottom_frame, text=f"{category}", font=("Arial", 10), fg="#555", bg="#e0e3cf").pack(
            side="left")
        tk.Label(bottom_frame, text=f"{created_at}", font=("Arial", 10), fg="#555", bg="#e0e3cf").pack(side="right")

    def count_transactions(self, user_id):
        response = get_transactions(user_id)
        message = response.get("message", "")
        match = re.search(r"(\d+)", message)
        return int(match.group(1))
