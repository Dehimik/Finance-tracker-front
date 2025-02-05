import tkinter as tk
import requests
from tkinter import messagebox

from app.assets.styles.styles import default_styles
from app.services.api_client import create_transaction

class TransactionNew(tk.Frame):
    def __init__(self, master, user_id):
        super().__init__(master)
        self.pack()
        self.create_widgets(user_id)
        default_styles(self)

    def create_widgets(self, user_id):
        tk.Label(self, text="Description").pack()
        self.desc_enty = tk.Entry(self)
        self.desc_enty.pack()

        tk.Label(self, text="Category").pack()
        self.cat_enty = tk.Entry(self)
        self.cat_enty.pack()

        tk.Label(self, text="Type(income/expence)").pack()
        self.type_enty = tk.Entry(self)
        self.type_enty.pack()

        tk.Label(self, text="Amount").pack()
        self.amount_enty = tk.Entry(self)
        self.amount_enty.pack()

        tk.Label(self, text="Payment method(cash/card)").pack()
        self.pay_enty = tk.Entry(self)
        self.pay_enty.pack()

        tk.Button(self, text="Add transaction", command=lambda: self.create_transaction(user_id)).pack()

    def create_transaction(self, user_id):
        description = self.desc_enty.get()
        category = self.cat_enty.get()
        type_ie = self.type_enty.get()
        amount = self.amount_enty.get()
        payment_method = self.pay_enty.get()

        try:
            response = create_transaction(user_id, description, category, type_ie, float(amount), payment_method)
            print(response)
            if response.get("status") == 200:
                messagebox.showinfo("Success!", "Transaction successfully added!")
                self.master.trans_id = response.get("data", {}).get("transaction_id")
                self.master.show_home()
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Shit happens: {e}")

    def show_home(self):
        self.master.show_home()