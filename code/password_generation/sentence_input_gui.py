"""
This module contains everything related to the GUI part of generating a password passed on an inputted sentence.
"""
import tkinter as tk
from PIL import ImageTk, Image
import customtkinter
import string

import password_generation.sentence_input_logic as logic


class SentenceInputToplevel(customtkinter.CTkToplevel):
    """
    This class creates the sentence input toplevel
    """
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        """
        Called upon starting the app,
        this function prepares the 'input sentence' frame for when
        the user wants to try other methods of password generation
        by creating a basic Tkinter configuration, with an instruction, input,
        and a way to display the produced password.
        """
        self.geometry('830x280')
        self.title('Sentence input')
        # Load the icon image
        icon_image = Image.open('textures/logo.ico')
        icon_photo = ImageTk.PhotoImage(icon_image)

        # Set the icon photo
        self.wm_iconphoto(False, icon_photo)

        self.grid_rowconfigure(0, weight=1, uniform='row')
        self.grid_rowconfigure(1, weight=1, uniform='row')
        self.grid_rowconfigure(2, weight=1, uniform='row')
        self.grid_rowconfigure(3, weight=1, uniform='row')
        self.grid_rowconfigure(4, weight=1, uniform='row')
        self.grid_columnconfigure(0, weight=1, uniform='column')

        self.instruction_font = customtkinter.CTkFont(family='Roboto', size=24)
        self.warning_font = customtkinter.CTkFont(family='Roboto', size=20)
        self.word_font = customtkinter.CTkFont(family='Roboto', size=14)

        self.instruction_label = customtkinter.CTkLabel(master=self, text='Input a sentence',
                                                        font=self.instruction_font)
        self.instruction_label.grid(row=0, column=0)

        self.input_box = customtkinter.CTkEntry(self, width=700, corner_radius=8)
        self.input_box.grid(row=1, column=0)

        self.password_label = customtkinter.CTkTextbox(self, font=self.word_font, width=500, height=50, wrap='word')
        self.password_label.grid(row=2, column=0)

        self.warning_label_1 = customtkinter.CTkLabel(master=self, font=self.warning_font)
        self.warning_label_2 = customtkinter.CTkLabel(master=self, font=self.warning_font)
        self.warning_labels = [self.warning_label_1, self.warning_label_2]

        self.password_label.tag_config('red', foreground='red')

        def highlight_sentence():
            """
            Called as the user types,
            this function calls the produce_password function of sentence_input_logic.py
            to get a password based on the user's sentence,
            and displays it on the screen.
            """
            char_dict = {}
            letters_to_be_coloured = {}

            self.password_label.delete('1.0', 'end')
            self.password_label.insert('1.0', self.input_box.get())

            for i, char in enumerate(self.input_box.get()):
                if char.isspace():
                    char_dict[i] = "space"
                else:
                    char_dict[i] = char

            first_letter_taken = False
            for key, value in char_dict.items():
                if value in string.punctuation or value in string.digits:
                    letters_to_be_coloured[f'1.{key}'] = f'1.{key + 1}'
                elif value == 'space':
                    first_letter_taken = False
                elif not first_letter_taken:
                    letters_to_be_coloured[f'1.{key}'] = f'1.{key + 1}'
                    first_letter_taken = True

            for key, value in letters_to_be_coloured.items():
                self.password_label.tag_add('red', key, value)

        self.input_box.bind('<Return>', highlight_sentence)

        def close_second_window():
            """
            This function destroys the window when it is closed.
            """
            self.destroy()
            self.master.deiconify()

        self.protocol("WM_DELETE_WINDOW", close_second_window)
