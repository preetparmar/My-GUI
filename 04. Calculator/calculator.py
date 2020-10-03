# Importing Libraries
import tkinter as tk

# Defining Colors
dark_green = '#93af22'
light_green = '#acc253'
white_green = '#edefe0'

# Defining Fonts
button_font = ('Arial', 18)
display_font = ('Arial', 30)

# Defining Functions
def submit_number(number):
    """ Add a number or decimal to the display """
    # Insert the number or decimal pressed to the end of the display
    display.insert(tk.END, number)

    # If decimal was pressed, disable the decimal button so it can't be pressed
    if '.' in display.get():
        decimal_button.config(state=tk.DISABLED)

def clear():
    display.delete(0, tk.END)
    enable_buttons()

def operate(operator):
    """ Store the first number and operator to be used """
    global first_num, operation

    # Get the first number and operator
    first_num = display.get()
    operation = operator

    # Clear the Entry Label
    display.delete(0, tk.END)

    # Disable all operators untill equal or clear is pressed
    disable_buttons()

    # Return Decimal button to normal state
    decimal_button.config(state=tk.NORMAL)

def equal():
    global value, first_num

    """ Run the stored operation for two number """
    # Perform desired mathematics
    if operation == 'add':
        value = float(first_num) + float(display.get())
    elif operation == 'substract':
        value = float(first_num) - float(display.get())
    elif operation == 'multiply':
        value = float(first_num) * float(display.get())
    elif operation == 'divide':
        if display.get() == '0':
            value = 'ERROR'
        else:
            value = float(first_num) / float(display.get())
    elif operation == 'exponent':
        value = float(first_num) ** float(display.get())
    
    # Remove the current value and display the value
    display.delete(0, tk.END)
    display.insert(0, value)
    # first_num = value

    # Enalble buttons to normal state
    enable_buttons()

def disable_buttons():
    add_button.config(state=tk.DISABLED)
    substract_button.config(state=tk.DISABLED)
    multiply_button.config(state=tk.DISABLED)
    divide_button.config(state=tk.DISABLED)
    exponent_button.config(state=tk.DISABLED)
    inverse_button.config(state=tk.DISABLED)
    square_button.config(state=tk.DISABLED)

def enable_buttons():
    decimal_button.config(state=tk.NORMAL)
    add_button.config(state=tk.NORMAL)
    substract_button.config(state=tk.NORMAL)
    multiply_button.config(state=tk.NORMAL)
    divide_button.config(state=tk.NORMAL)
    exponent_button.config(state=tk.NORMAL)
    inverse_button.config(state=tk.NORMAL)
    square_button.config(state=tk.NORMAL)

def inverse():
    if display.get() == '0':
        value = 'ERROR'
    else:
        value = 1/float(display.get())
    
    # Remove the value in display and insert the inverted value
    display.delete(0, tk.END)
    display.insert(0, value)

def square():
    value = float(display.get()) ** 2

    # Remove the value in display and insert the inverted value
    display.delete(0, tk.END)
    display.insert(0, value)

def negate():
    value = -float(display.get())
    # Remove the value in display and insert the inverted value
    display.delete(0, tk.END)
    display.insert(0, value)

# Defining Root Window
root = tk.Tk()
root.title('Calculator')
root.iconbitmap(r'04. Calculator\Assets\calc.ico')
root.geometry('300x400+1400+400')
root.resizable(0, 0)

# Defining Frames
display_frame = tk.LabelFrame(root)
button_frame = tk.LabelFrame(root)

display_frame.pack(padx=2, pady=(5, 20))
button_frame.pack(padx=2, pady=5)

# Layout for Display Frame
display = tk.Entry(display_frame, width=50, font=display_font, bg=white_green, borderwidth=5, justify='right')
display.pack()
display.focus_set()  # sets focus to entry at the beggining of the program

# Layout for Button Frame
clear_button = tk.Button(button_frame, text= 'Clear', font=button_font, bg=light_green, command=clear)
quit_button = tk.Button(button_frame, text='Quit', font=button_font, bg=light_green, command=root.destroy)

inverse_button = tk.Button(button_frame, text='1/x', font=button_font, bg=light_green, command=inverse)
square_button = tk.Button(button_frame, text='x^2', font=button_font, bg=light_green, command=square)
exponent_button = tk.Button(button_frame, text='x^n', font=button_font, bg=light_green, command=lambda: operate('exponent'))
divide_button = tk.Button(button_frame, text=' / ', font=button_font, bg=light_green, command=lambda: operate('divide'))
multiply_button = tk.Button(button_frame, text='*', font=button_font, bg=light_green, command=lambda: operate('multiply'))
substract_button = tk.Button(button_frame, text='-', font=button_font, bg=light_green, command=lambda: operate('substract'))
add_button = tk.Button(button_frame, text='+', font=button_font, bg=light_green, command=lambda: operate('add'))
equal_button = tk.Button(button_frame, text='=', font=button_font, bg=dark_green, command=equal)
decimal_button = tk.Button(button_frame, text='.', font=button_font, bg='black', fg='white', command=lambda: submit_number('.'))
negate_button = tk.Button(button_frame, text='+/-', font=button_font, bg='black', fg='white', command=negate)

nine_button = tk.Button(button_frame, text='9', font=button_font, bg='black', fg='white', command=lambda: submit_number(9))
eigth_button = tk.Button(button_frame, text='8', font=button_font, bg='black', fg='white', command=lambda: submit_number(8))
seven_button = tk.Button(button_frame, text='7', font=button_font, bg='black', fg='white', command=lambda: submit_number(7))
six_button = tk.Button(button_frame, text='6', font=button_font, bg='black', fg='white', command=lambda: submit_number(6))
five_button = tk.Button(button_frame, text='5', font=button_font, bg='black', fg='white', command=lambda: submit_number(5))
four_button = tk.Button(button_frame, text='4', font=button_font, bg='black', fg='white', command=lambda: submit_number(4))
three_button = tk.Button(button_frame, text='3', font=button_font, bg='black', fg='white', command=lambda: submit_number(3))
two_button = tk.Button(button_frame, text='2', font=button_font, bg='black', fg='white', command=lambda: submit_number(2))
one_button = tk.Button(button_frame, text='1', font=button_font, bg='black', fg='white', command=lambda: submit_number(1))
zero_button = tk.Button(button_frame, text='0', font=button_font, bg='black', fg='white', command=lambda: submit_number(0))

# First Row
clear_button.grid(row=1, column=1, columnspan=2, pady=1, sticky='we')
quit_button.grid(row=1, column=3, columnspan=2, pady=1, sticky='we')

# Second Row
inverse_button.grid(row=2, column=1, pady=1, sticky='we')
square_button.grid(row=2, column=2, pady=1, sticky='we')
exponent_button.grid(row=2, column=3, pady=1, sticky='we')
divide_button.grid(row=2, column=4, pady=1, sticky='we')

# Third Row
seven_button.grid(row=3, column=1, pady=1, sticky='we', ipadx=20)
eigth_button.grid(row=3, column=2, pady=1, sticky='we', ipadx=20)
nine_button.grid(row=3, column=3, pady=1, sticky='we', ipadx=20)
multiply_button.grid(row=3, column=4, pady=1, sticky='we', ipadx=20)

# Fourth Row
four_button.grid(row=4, column=1, pady=1, sticky='we')
five_button.grid(row=4, column=2, pady=1, sticky='we')
six_button.grid(row=4, column=3, pady=1, sticky='we')
substract_button.grid(row=4, column=4, pady=1, sticky='we')

# Fifth Row
one_button.grid(row=5, column=1, pady=1, sticky='we')
two_button.grid(row=5, column=2, pady=1, sticky='we')
three_button.grid(row=5, column=3, pady=1, sticky='we')
add_button.grid(row=5, column=4, pady=1, sticky='we')

# Sixth Row
negate_button.grid(row=6, column=1, pady=1, sticky='we')
zero_button.grid(row=6, column=2, pady=1, sticky='we')
decimal_button.grid(row=6, column=3, pady=1, sticky='we')
equal_button.grid(row=6, column=4, pady=1, sticky='we')

# Running Root Mainloop
root.mainloop()