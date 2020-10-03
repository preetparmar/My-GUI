# Importing Libraries
import tkinter as tk
from PIL import ImageTk, Image

# Defining Colors
root_color = '#224870'
input_color = '#2a4494'
output_color = '#4ea5d9'

# Defining Functions
def submit_name():
    text = name.get()
    if case_style.get() == 'normal':
        name_label = tk.Label(output_frame, text=f'Hello {text}! How are you today?')
    else:
        name_label = tk.Label(output_frame, text=f'Hello {text}! How are you today?'.upper())
    name_label.config(bg=output_color)
    name_label.pack()
    name.delete(0, tk.END)

# Defining Root Window
root = tk.Tk()
root.title('Hello GUI World')
root.iconbitmap(r'01. Hello GUI World\Assets\wave.ico')
root.geometry('400x400+1400+300')
root.resizable(0, 0)
root.config(bg=root_color)

"""DEFINING LAYOUTS"""
# Defining Frames
input_frame = tk.Frame(root, bg=input_color)
output_frame = tk.Frame(root, bg=output_color)

# Placing Frames
input_frame.pack(pady=10)
output_frame.pack(padx=10, pady=(0, 10), fill=tk.BOTH, expand=True)

"""CREATING WIDGETS"""
# Entry Widget
name = tk.Entry(input_frame, text='Enter your name:', width=20)
name.grid(row=0, column=0, padx=10, pady=10)

# Button Widget
submit_buttom = tk.Button(input_frame, text='Submit', command=submit_name)
submit_buttom.grid(row=0, column=1, padx=10, pady=10, ipadx=20)

# Radio Button
case_style = tk.StringVar()
case_style.set('normal')
normal_button = tk.Radiobutton(input_frame, text='Normal Case', variable=case_style, value='normal', bg=input_color)
normal_button.grid(row=1, column=0, padx=2, pady=2)
upper_button = tk.Radiobutton(input_frame, text='Upper Case', variable=case_style, value='upper', bg=input_color)
upper_button.grid(row=1, column=1, padx=2, pady=2)

""" CREATING OUTPUTS """
# Smile PNG
smile_image = ImageTk.PhotoImage(Image.open(r'01. Hello GUI World\Assets\smile.png'))
smile_label = tk.Label(output_frame, image=smile_image, bg=output_color)
smile_label.pack()


# Running your mainloop
root.mainloop()