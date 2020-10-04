# Importing Libraries
import tkinter as tk
from PIL import ImageTk, Image
from tkinter.scrolledtext import ScrolledText
from tkinter.messagebox import askyesno
from tkinter.filedialog import asksaveasfilename, askopenfilename

# Defining Colors
text_color = '#fffacd'
menu_color = '#dbd9db'
root_color = '#6c809a'


# Defining Functions
def change_font(event):
    global my_font
    if font_style.get() == 'Regular':
        my_font = (font_family.get(), font_size.get())
    else:
        my_font = (font_family.get(), font_size.get(), font_style.get().lower())
    
    input_text.config(font=my_font)

def new_note():
    question = askyesno('New Note', 'Are you sure you want to start a new note?')
    if question == 1:
        input_text.delete(1.0, tk.END)
    else:
        return

def close_note():
    question = askyesno('Close Note', 'Are you sure you want to quit?')
    if question == 1:
        root.destroy()
    else:
        return

def save_note():
    save_name = asksaveasfilename(initialdir='./', title='Save Note', filetypes=(('Text Files', '*.txt'), ('All Files', '*.*')))
    with open(save_name, 'w') as file:
        file.write(f'{font_family.get()}\n{str(font_size.get())}\n{font_style.get()}\n')
        file.write(input_text.get(1.0, tk.END))

        
def open_note():
    open_name = askopenfilename(initialdir='./', title='Open Note', filetypes=(('Text Files', '*.txt'), ('All Files', '*.*')))
    input_text.delete(1.0, tk.END)

    with open(open_name, 'r') as file:
        font_family.set(file.readline().strip())
        font_size.set(int(file.readline().strip()))
        font_style.set(file.readline().strip())
        change_font(1)

        text = file.read()
    input_text.insert(1.0, text)


# Defining Root Window
root = tk.Tk()
root.title('Notepad')
root.iconbitmap(r'05. Notepad\Assets\pad.ico')
root.geometry('600x600+1400+400')
root.resizable(0, 0)
root.config(bg=root_color)

# Defining Layouts
menu_frame = tk.Frame(root, bg=menu_color)
text_frame = tk.Frame(root, bg=text_color)

menu_frame.pack(padx=5, pady=5)
text_frame.pack(padx=5, pady=5)

# Defining Images
new_image = ImageTk.PhotoImage(Image.open(r'05. Notepad\Assets\new.png'))
open_image = ImageTk.PhotoImage(Image.open(r'05. Notepad\Assets\open.png'))
save_image = ImageTk.PhotoImage(Image.open(r'05. Notepad\Assets\save.png'))
close_image = ImageTk.PhotoImage(Image.open(r'05. Notepad\Assets\close.png'))


# Layout for Menu Frame
new_button = tk.Button(menu_frame, image=new_image, command=new_note)
open_button = tk.Button(menu_frame, image=open_image, command=open_note)
save_button = tk.Button(menu_frame, image=save_image, command=save_note)
close_button = tk.Button(menu_frame, image=close_image, command=close_note)

new_button.grid(row=1, column=1, padx=5, pady=5)
open_button.grid(row=1, column=2, padx=5, pady=5)
save_button.grid(row=1, column=3, padx=5, pady=5)
close_button.grid(row=1, column=4, padx=5, pady=5)

# Defining Font Dropdown
families = ['Terminal', 'Modern', 'Script', 'Courier', 'Arial', 'Calibri', 'Cambria', 'Georgia', 'MS Gothic', 'SimSun', 'Tahona', 'Times New Roman', 'Verdana', 'Windings']
font_family = tk.StringVar()
font_family_drop = tk.OptionMenu(menu_frame, font_family, *families, command=change_font)
font_family.set(families[0])
font_family_drop.config(width=16)  # fits the longest font and the width stays consistent
font_family_drop.grid(row=1, column=5, padx=5, pady=5)

# Defining Font Size Dropdown
sizes = [8, 10, 12, 14, 16, 20, 24, 32, 34, 36]
font_size = tk.IntVar()
font_size_drop = tk.OptionMenu(menu_frame, font_size, *sizes, command=change_font)
font_size_drop.config(width=2)
font_size.set(sizes[2])
font_size_drop.grid(row=1, column=6, padx=5, pady=5)

# Defining Font Stype Dropdown
styles = ['Regular', 'Bold', 'Italic']
font_style = tk.StringVar()
font_style_drop = tk.OptionMenu(menu_frame, font_style, *styles, command=change_font)
font_style_drop.config(width=8)
font_style.set(styles[0])
font_style_drop.grid(row=1, column=7, padx=5, pady=5)

# Defining Text Frame Layout
my_font = (font_family.get(), font_size.get())
input_text = ScrolledText(text_frame, bg=text_color, font=my_font, width=100, height=100)
input_text.focus_set()
input_text.pack()

# Running Root Mainloop
root.mainloop()