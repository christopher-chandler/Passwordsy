"""
This module prepares the other_methods_window for the user when they click the 'try other methods...' button.
"""
import tkinter as tk
from tkinter.font import Font
import customtkinter

from password_generation import diceware_gui as diceware
from password_generation import sentence_input_gui as sentence_input


class CreateToolTip:
    """
    This class creates a tooltip for a given widget and text.
    """

    def __init__(self, widget, text='widget info'):
        self.waittime = 500  # miliseconds
        self.wraplength = 180  # pixels
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)
        self.id = None
        self.tw = None

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showtip)

    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)

    def showtip(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        # creates a toplevel window
        self.tw = tk.Toplevel(self.widget)
        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(self.tw, text=self.text, justify='left',
                         background="#ffffff", relief='solid', borderwidth=1,
                         wraplength=self.wraplength)
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tw
        self.tw = None
        if tw:
            tw.destroy()


class OtherMethodsWindow(customtkinter.CTkToplevel):
    """
    This class contains the creation of the 'other methods' Toplevel window
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.button_border_width = 2
        self.button_fg_color = 'blue'
        self.button_hover_color = 'gray'
        self.button_border_color = 'black'

        self.medium_button_font = customtkinter.CTkFont(family='Roboto', size=24)
        self.title_font = customtkinter.CTkFont(family='Roboto', size=36)

        self.window_title = 'Try other methods...'

        self.iconbitmap('textures/logo.ico')
        self.geometry('700x250')
        self.title(self.window_title)

        self.frame_title = customtkinter.CTkLabel(master=self, text='How to generate a password?',
                                                  font=self.title_font)
        self.frame_title.grid(column=0, row=0, columnspan=3)

        self.question_mark = customtkinter.CTkLabel(master=self, text='❓', font=self.title_font)
        self.question_mark.grid(column=0, row=1, sticky='e', padx=10)
        self.question_mark_ttp = CreateToolTip(self.question_mark, 'Roll 5 dice to form a 5-digit number '
                                                                   'that will be matched to a word on a list')

        self.diceware_btn = customtkinter.CTkButton(self,
                                                    text='From the diceware wordlist',
                                                    command=self.open_diceware,
                                                    font=self.medium_button_font,
                                                    border_width=self.button_border_width,
                                                    border_color=self.button_border_color,
                                                    fg_color=self.button_fg_color,
                                                    hover_color=self.button_hover_color)
        self.diceware_btn.grid(row=1, column=1, pady=10, sticky='w')

        self.sentence_input_btn = customtkinter.CTkButton(self,
                                                          text='From a sentence',
                                                          command=self.open_sentence_input,
                                                          font=self.medium_button_font,
                                                          border_width=self.button_border_width,
                                                          border_color=self.button_border_color,
                                                          fg_color=self.button_fg_color,
                                                          hover_color=self.button_hover_color)
        self.sentence_input_btn.grid(row=1, column=2, pady=10, sticky='w')

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1, uniform='column')

        self.diceware_window = None
        self.sentence_input_window = None

        self.withdraw()
        self.after(200, self.show_icon)

    def show_icon(self):
        """
        This function shows the icon of the toplevel window.
        """
        self.deiconify()
        self.iconbitmap('textures/logo.ico')

    def open_diceware(self):
        """
        Called when the user clicks on the 'From the diceware' button,
        this function opens the diceware Toplevel window.
        """
        self.withdraw()
        if self.diceware_window is None or not self.diceware_window.winfo_exists():
            self.diceware_window = diceware.DicewareToplevel(self)
        else:
            self.diceware_window.focus()

    def open_sentence_input(self):
        """
        Called when the user clicks on the 'From a sentence' button,
        this function opens the sentence input Toplevel window.
        """
        self.withdraw()
        if self.sentence_input_window is None or not self.sentence_input_window.winfo_exists():
            self.sentence_input_window = sentence_input.SentenceInputToplevel(self)
        else:
            self.sentence_input_window.focus()
