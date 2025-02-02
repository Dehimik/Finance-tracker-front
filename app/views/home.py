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
        tk.Label(self, text="nickname").pack()

        #transactions = get_transactions()
        #for transaction in transactions:
            #self.create_transaction_card(self, transaction)

        tk.Button(self, text = "Profile", command = self.open_profile).pack()
        tk.Label(self, text="BALANCE HERE").pack()

    def open_profile(self):
        self.master.show_profile()

    def create_transaction_card(self, parent, transaction):
        # Create cool card here
        card = tk.Frame(parent, bg="#e0e3cf", padx=10, pady=10)
        card.pack(fill="x", padx=15, pady=5)

        # Top: Name+amount
        top_frame = tk.Frame(card, bg="#e0e3cf")
        top_frame.pack(fill="x")

        tk.Label(top_frame, text=transaction["category"], font=("Arial", 14, "bold"), bg="#e0e3cf").pack(side="left")
        tk.Label(top_frame, text=transaction["amount"], font=("Arial", 14, "bold"), fg="#004225", bg="#e0e3cf").pack(
            side="right")

        # Bottom: Category+time
        bottom_frame = tk.Frame(card, bg="#e0e3cf")
        bottom_frame.pack(fill="x")

        tk.Label(bottom_frame, text=transaction["category"], font=("Arial", 10), fg="#555", bg="#e0e3cf").pack(
            side="left")
        tk.Label(bottom_frame, text=transaction["time"], font=("Arial", 10), fg="#555", bg="#e0e3cf").pack(side="right")
