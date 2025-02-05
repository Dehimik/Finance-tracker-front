import tkinter as tk

from app.views.profile import ProfileWindow
from views.login import LoginWindow
from views.register import RegisterWindow
from views.home import HomeWindow
from views.profile_edit import ProfileEdit

from assets.styles.styles import default_styles

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Finance Tracker")
        self.geometry("500x300")
        self.current_frame = None
        self.user_id = None
        default_styles(self)
        self.show_login()

    def show_login(self):
        self.switch_frame(LoginWindow)

    def show_register(self):
        self.switch_frame(RegisterWindow)

    def show_home(self):
        self.switch_frame(HomeWindow, self.user_id)

    def show_profile(self):
        self.switch_frame(ProfileWindow, self.user_id)

    def show_edit_profile(self):
        self.switch_frame(ProfileEdit, self.user_id)

    def switch_frame(self, frame_class, *args):
        # Clear frame and switch it to other frame
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = frame_class(self, *args)
        self.current_frame.pack()

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()