import tkinter as tk
from views.login import LoginWindow
from views.register import RegisterWindow

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("My App")
        self.geometry("400x300")
        self.current_frame = None
        self.show_login()

    def show_login(self):
        self.switch_frame(LoginWindow)

    def show_register(self):
        self.switch_frame(RegisterWindow)

    def switch_frame(self, frame_class):
        """Очищає поточний фрейм та завантажує новий."""
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = frame_class(self)
        self.current_frame.pack()

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()