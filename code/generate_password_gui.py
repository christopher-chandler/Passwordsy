import tkinter as tk

import generate_password_logic as logic

title_font = 'Helvetica 24'
section_title_font = 'Helvetica 16'
description_font = 'Helvetica 12'

password_width = 100
password_height = 1
password_border_width = 0
password_font = 'Consolas 11'

invalid_input_error = 'An error occurred. Try again with a whole number between 4 and 100.'
no_character_set_error = 'An error occurred. Try again with at least 1 character set.'
double_error = 'An error occurred. Try again with at least 1 character set and a whole number between 4 and 100.'


def create_generate_password_frame(frame, done_btn_image) -> None:
    '''
    Called upon starting the program,
    this function uses the Tkinter module to create a GUI frame to generate passwords with various options for customisation
    (length and character sets),
    and serves as a hub for all other password generation functions.

    Parameters
    ----------
    frame: ttk.frame
        The "generate password" frame upon which the objects of this function will be placed.
    done_btn_image: ImageTk.PhotoImage
        The image used for the done button.
    '''
    password_label_1 = tk.Text(frame, width=password_width, height=password_height,
                               borderwidth=password_border_width, font=password_font)
    password_label_2 = tk.Text(frame, width=password_width, height=password_height,
                               borderwidth=password_border_width, font=password_font)
    password_label_3 = tk.Text(frame, width=password_width, height=password_height,
                               borderwidth=password_border_width, font=password_font)
    password_label_4 = tk.Text(frame, width=password_width, height=password_height,
                               borderwidth=password_border_width, font=password_font)
    password_labels = [password_label_1, password_label_2, password_label_3, password_label_4]
    
    frame_title = tk.Label(frame, text='Generate password', font=title_font)
    frame_title.grid(column=0, row=1, columnspan=2)

    question = tk.Label(frame, text='Number of characters (4 to 100):', font=description_font)
    question.grid(column=0, row=2, columnspan=2)

    character_sets_label = tk.Label(frame, text='Character sets', font=section_title_font)
    character_sets_label.grid(column=1, row=4, columnspan=2)

    lowercase_letters_var = tk.IntVar()
    lowercase_letters_checkbox = tk.Checkbutton(frame, variable=lowercase_letters_var, offvalue=0, onvalue=1)
    lowercase_letters_text = tk.Label(frame, text='Lowercase letters', font=description_font)

    uppercase_letters_var = tk.IntVar()
    uppercase_letters_checkbox = tk.Checkbutton(frame, variable=uppercase_letters_var, offvalue=0, onvalue=1)
    uppercase_letters_text = tk.Label(frame, text='Uppercase letters', font=description_font)

    digits_var = tk.IntVar()
    digits_checkbox = tk.Checkbutton(frame, variable=digits_var, offvalue=0, onvalue=1)
    digits_text = tk.Label(frame, text='Digits', font=description_font)

    punctuation_var = tk.IntVar()
    punctuation_checkbox = tk.Checkbutton(frame, variable=punctuation_var, offvalue=0, onvalue=1)
    punctuation_text = tk.Label(frame, text='Punctuation', font=description_font)

    checkboxes = [lowercase_letters_checkbox, uppercase_letters_checkbox, digits_checkbox, punctuation_checkbox]
    checkboxes_text_labels = [lowercase_letters_text, uppercase_letters_text, digits_text, punctuation_text]

    for checkbox in checkboxes:
        checkbox.grid(column=1, row=5 + checkboxes.index(checkbox), pady=8)
        checkbox.select()
    
    for text in checkboxes_text_labels:
        text.grid(column=2, row=5 + checkboxes_text_labels.index(text), sticky='w')

    def create_password_labels(event) -> None:
        '''
        Called upon clicking the done button or pressing the ENTER key,
        this function calls determine_error and validate_character_sets of generate_password_logic,
        and then settles whether an error has occurred or not.
        If an error has occurred, the function displays said error 
        (obtained through determine_error),
        and displays it on the screen through show_text.
        If an error has not occurred, the function calls generate_password of generate_password_logic.py to get 4 passwords,
        and calls the show_text function to display them to the user.

        Parameters
        ----------
        event:
            Necessary for initiating the function when pressing the ENTER key.
        '''
        for password_label in password_labels:
                password_label.bind('<ButtonRelease>', lambda event: logic.show_copy_button(event, copy_button))

        text = logic.determine_error(logic.validate_character_sets(lowercase_letters_var, uppercase_letters_var, digits_var, punctuation_var), 
                                                input_box.get(), no_character_set_error, double_error, invalid_input_error)

        # Check if an error was not returned
        if text == '':
            for password_label in password_labels:
                adapted_input = logic.adapt_input(input_box.get())
                input_box.delete(0, 'end')
                input_box.insert(1, adapted_input)

                text = logic.generate_password(adapted_input, lowercase_letters_var, uppercase_letters_var, digits_var, punctuation_var)
                show_text(password_label, text)
                password_label.grid(column=0, row=5 + password_labels.index(password_label), pady=10, padx=10)
        else:
            input_box.delete(0, 'end')
            password_label_1.grid(column=0, row=5, padx=10, pady=10)
            show_text(password_label_1, text)

    global input_box
    input_box = tk.Entry(frame, width=10, borderwidth=2)
    input_box.bind('<Return>', create_password_labels)
    input_box.grid(column=0, row=3, columnspan=2)

    done_btn = tk.Button(frame, image=done_btn_image, borderwidth=0, command=lambda: create_password_labels(None))
    done_btn.grid(column=0, row=4, columnspan=2)

    copy_button = tk.Menu(frame, tearoff=False)
    copy_button.add_command(label='Copy', command=lambda: logic.copy_text(input_box, password_labels))

    def show_text(label, text) -> None:
        '''
        Called by the create_password_labels function,
        this function updates the contents of the password_labels,
        by enabling the label, deleting its current contents, 
        inserting the new text, and then disabling the label again.

        Parameters
        ----------
        label: tkinter.Text
            Each password label one by one if passwords are generated,
            or the first password label if an error is generated.
        text: str
            Each password or the error.
        '''
        label.config(state='normal')
        label.delete('1.0', 'end')
        label.insert('1.0', text)
        label.config(state='disabled', bg='#ffffff')


def select_input_box(event) -> None:
    '''
    Called whenever the tab is changed,
    this function focuses the keyboard to the input box,
    which allows the user to start typing immediately without having to click on the input box first.
    '''
    input_box.focus()
