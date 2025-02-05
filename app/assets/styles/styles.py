import os
from tkinter import ttk
import tkinter.font as tkFont

def load_font(size=14):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Папка styles
    FONT_PATH = os.path.join(BASE_DIR, "../assets/fonts/LeagueGothic-Regular-VariableFont_wdth.ttf")
    try:
        return tkFont.Font(file=FONT_PATH, size=size)
    except Exception as e:
        return ("Arial", size)

def default_styles(root):
    style = ttk.Style()

    # Buttons
    style.configure("PrimaryButton", font=load_font(size=14), bg="#191919", fg="#C0C3B0")
    style.configure("SecondaryButton", font=load_font(size=14), bg="#464E41", fg="#C0C3B0")

    # Text
    style.configure("HeaderH1", font = load_font(size=28))
    style.configure("HeaderH2", font = load_font(size=20))
    style.configure("HeaderH3", font = load_font(size=18))

    style.configure("BodyS", font = load_font(size=12))
    style.configure("BodyM", font = load_font(size=14))
    style.configure("BodyL", font = load_font(size=16))

    # Background
    root.configure(bg="#C0C3B0")