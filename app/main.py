import tkinter as tk
from tkinter import messagebox
import requests

API_LOGIN_URL = "https://example.com/api/login"  # Here API
API_REGISTER_URL = "https://example.com/api/register"

# send data to API
def login():
    nickname = login_nickname_entry.get().strip()
    password = login_password_entry.get().strip()

    if not nickname or not password:
        messagebox.showwarning("Error", "Fill all fields!")
        return

    payload = {"nickname": nickname, "password": password}

    try:
        response = requests.post(API_LOGIN_URL, json=payload)
        response.raise_for_status()  # check HTTP problems

        data = response.json()  # convert to JSON

        if "token" in data:  # Check to API send back token
            messagebox.showinfo("Success", "Login successfully!")
            print(f"Oh, token: {data['token']}")
        else:
            messagebox.showerror("Error", "Incorrect nickname or password!")

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"I cant move it move it anymore: {e}")

def register():
    email = register_email_entry.get().strip()
    nickname = register_nickname_entry.get().strip()
    password = register_password_entry.get().strip()
    confirm_password = confirm_password_entry.get().strip()

    if not email or not nickname or not password or not confirm_password:
        messagebox.showwarning("Error", "Fill all fields!")
        return

    if password != confirm_password:
        messagebox.showerror("Error", "Passwords doesnt match!")
        return

    payload = {"email": email, "nickname": nickname, "password": password}

    try:
        response = requests.post(API_REGISTER_URL, json=payload)
        response.raise_for_status()
        messagebox.showinfo("Success", "Register success! Login now.")
        show_login_window()  # Повертаємося до логіну

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Registration unsuccessfull: {e}")

# Open login window
def show_login_window():
    register_window.withdraw()
    login_window.deiconify()

# Open register window
def show_register_window():
    login_window.withdraw()
    register_window.deiconify()

# Login
login_window = tk.Tk()
login_window.title("Login")
login_window.geometry("300x250")

tk.Label(login_window, text="Nickname:").pack(pady=5)
login_nickname_entry = tk.Entry(login_window, width=30)
login_nickname_entry.pack(pady=5)

tk.Label(login_window, text="Password:").pack(pady=5)
login_password_entry = tk.Entry(login_window, width=30, show="*")
login_password_entry.pack(pady=5)

login_button = tk.Button(login_window, text="Login", command=login)
login_button.pack(pady=10)

register_button = tk.Button(login_window, text="Registration", command=show_register_window)
register_button.pack(pady=5)

# Register window
register_window = tk.Toplevel(login_window)
register_window.title("Registration")
register_window.geometry("300x300")
register_window.withdraw()

tk.Label(register_window, text="Email:").pack(pady=5)
register_email_entry = tk.Entry(register_window, width=30)
register_email_entry.pack(pady=5)

tk.Label(register_window, text="Nickname:").pack(pady=5)
register_nickname_entry = tk.Entry(register_window, width=30)
register_nickname_entry.pack(pady=5)

tk.Label(register_window, text="Password:").pack(pady=5)
register_password_entry = tk.Entry(register_window, width=30, show="*")
register_password_entry.pack(pady=5)

tk.Label(register_window, text="Retype password:").pack(pady=5)
confirm_password_entry = tk.Entry(register_window, width=30, show="*")
confirm_password_entry.pack(pady=5)

register_submit_button = tk.Button(register_window, text="Register", command=register)
register_submit_button.pack(pady=10)

back_to_login_button = tk.Button(register_window, text="Back", command=show_login_window)
back_to_login_button.pack(pady=5)

# Запуск Tkinter
login_window.mainloop()