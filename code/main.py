import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

import generate_password_gui
import password_strength_gui
import generate_password_logic


def main():
    '''
    Called upon starting the program,
    this function uses the Tkinter module to create a window, notebook, 
    two frames the user can switch between,
    and a basic configuration.
    '''
    window = tk.Tk()

    notebook = ttk.Notebook(window, width=1000, height=325)
    notebook.grid(column=0, row=0)

    # Center the notebook
    window.grid_columnconfigure(0, weight=1)
    window.grid_rowconfigure(0, weight=1)

    app_name = 'Passwordsy'

    window.iconphoto(False, tk.PhotoImage(file='logo.png'))
    window.title(app_name)

    done_btn_image = ImageTk.PhotoImage(Image.open('done_btn.png'))

    notebook.bind('<<NotebookTabChanged>>', generate_password_gui.select_input_box)
    window.bind('<Control-L>', lambda ab: generate_password_logic.hide_copy_button(None, generate_password_gui.copy_menu))

    class GeneratePasswordFrame:
        '''
        A class that creates the 'generate password' frame,
        and adds it to the notebook previously created.

        ...

        Attributes
        ----------
        generate_password_frame: ttk.frame
            The 'generate password' frame
        '''
        generate_password_frame = tk.Frame(window)
        generate_password_frame.grid(column=0, row=0)

        # Expand some widgets' rows and columns to take up the entire window
        generate_password_frame.grid_columnconfigure(0, weight=1)
        generate_password_frame.grid_rowconfigure(0, weight=1)
        generate_password_frame.grid_rowconfigure(1, weight=1)
        generate_password_frame.grid_rowconfigure(2, weight=1)
        generate_password_frame.grid_rowconfigure(3, weight=1)
        generate_password_frame.grid_rowconfigure(4, weight=1)

        notebook.add(generate_password_frame, text = 'Generate password')

        generate_password_gui.create_generate_password_frame(generate_password_frame, done_btn_image)

    class PasswordStrengthFrame:
        '''
        A class that creates the "password strength" frame,
        and adds it to the notebook previously created.
        ...

        Attributes
        ----------
        password_strength_frame: ttk.frame
            The password strength frame
        '''
        password_strength_frame = tk.Frame(notebook)
        password_strength_frame.grid(column=0, row=0)

        # Expand widgets to take up the entire window
        password_strength_frame.grid_columnconfigure(0, weight=1)
        password_strength_frame.grid_rowconfigure(0, weight=1)
        password_strength_frame.grid_rowconfigure(1, weight=1)
        password_strength_frame.grid_rowconfigure(2, weight=1)
        password_strength_frame.grid_rowconfigure(3, weight=1)
        password_strength_frame.grid_rowconfigure(4, weight=1)
        password_strength_frame.grid_rowconfigure(5, weight=1)
        password_strength_frame.grid_rowconfigure(6, weight=1)


        notebook.add(password_strength_frame, text = 'Password strength')

        password_strength_gui.create_password_strength_frame(password_strength_frame)

    window.mainloop()


if __name__ == '__main__':
    exit(main())
