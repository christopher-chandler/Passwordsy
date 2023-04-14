"""
This is the main module of Passwordsy.
"""
import tkinter as tk
from abc import ABC
from tkinter import ttk
from PIL import ImageTk, Image
import customtkinter

from password_generation import generate_password_gui
from password_strength import password_strength_gui


class TabView(customtkinter.CTkTabview, ABC):
    """
    This class creates the tabview of the app.
    """
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(width=1200, height=485)

        # Create the 2 tabs
        self.add('Generate password')
        self.add('Password strength')

        self.generate_password_frame = generate_password_gui.PasswordGenerationFrame(
            master=self.tab('Generate password'))
        self.generate_password_frame.pack(fill='both', expand=1)
        self.generate_password_frame.configure(fg_color=('#DBDBDB', '#2B2B2B'))

        # Expand some widgets' rows and columns to take up the entire window
        self.generate_password_frame.grid_columnconfigure(0, weight=1)
        i = 0
        self.generate_password_frame.grid_rowconfigure(0, weight=1)
        self.generate_password_frame.grid_rowconfigure(1, weight=1)
        self.generate_password_frame.grid_rowconfigure(2, weight=1)
        self.generate_password_frame.grid_rowconfigure(3, weight=1)
        self.generate_password_frame.grid_rowconfigure(4, weight=1)
        self.generate_password_frame.grid_rowconfigure(5, weight=1)
        self.generate_password_frame.grid_rowconfigure(6, weight=1)
        self.generate_password_frame.grid_rowconfigure(7, weight=1)
        self.generate_password_frame.grid_rowconfigure(8, weight=1)
        # To prevent lag
        self.generate_password_frame.grid_propagate(False)

        # Create the password strength frame
        self.password_strength_frame = password_strength_gui.PasswordStrengthFrame(master=self.tab('Password strength'))
        self.password_strength_frame.pack(fill='both', expand=1)
        self.password_strength_frame.configure(fg_color=('#DBDBDB', '#2B2B2B'))

        # Expand widgets to take up the entire window
        self.password_strength_frame.grid_columnconfigure(0, weight=1)
        i = 0
        while i <= 6:
            self.password_strength_frame.grid_rowconfigure(i, weight=1)
            i += 1


def resize(root_window, event=None):
    """
    This function aims to reduce resizing lag.
    """
    root_window.update_idletasks()


class App(customtkinter.CTk):
    """
    This class creates the app itself.
    """
    def __init__(self):
        super().__init__()

        # Center the notebook
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.iconbitmap('textures/logo.ico')
        self.geometry('1200x485')

        app_name = 'Passwordsy'
        self.title(app_name)

        self.tab_view = TabView(master=self)
        self.tab_view.grid(column=0, row=0)

        self.bind('<Configure>', lambda a: resize(self))


def main():
    """
    Called upon starting the program,
    this function uses the Tkinter module to create a window, notebook,
    two frames the user can switch between,
    and a basic configuration.
    """
    global root
    root = App()
    root.mainloop()


if __name__ == '__main__':
    exit(main())
