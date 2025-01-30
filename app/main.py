import tkinter as tk
from tkinter import messagebox
import requests

API_URL = "https://example.com/api/login"  # Замінити на справжню адресу API

# Функція для відправки даних на API
def login():
    email = email_entry.get().strip()
    password = password_entry.get().strip()

    if not email or not password:
        messagebox.showwarning("Помилка", "Заповніть всі поля!")
        return

    payload = {"email": email, "password": password}

    try:
        response = requests.post(API_URL, json=payload)
        response.raise_for_status()  # Перевіряє HTTP помилки

        data = response.json()  # Перетворюємо відповідь API у JSON

        if "token" in data:  # Перевіряємо, чи повернув API токен
            messagebox.showinfo("Успіх", "Логін успішний!")
            print(f"Отриманий токен: {data['token']}")  # Можна зберегти токен
        else:
            messagebox.showerror("Помилка", "Невірний email або пароль!")

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Помилка", f"Не вдалося виконати запит: {e}")

# Головне вікно
root = tk.Tk()
root.title("Авторизація")
root.geometry("300x200")

# Поле для введення email
tk.Label(root, text="Email:").pack(pady=5)
email_entry = tk.Entry(root, width=30)
email_entry.pack(pady=5)

# Поле для введення пароля
tk.Label(root, text="Пароль:").pack(pady=5)
password_entry = tk.Entry(root, width=30, show="*")  # Приховуємо пароль
password_entry.pack(pady=5)

# Кнопка "Увійти"
login_button = tk.Button(root, text="Увійти", command=login)
login_button.pack(pady=10)

# Запуск Tkinter
root.mainloop()