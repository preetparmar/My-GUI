# Importing Library
import tkinter as tk

# Defining Fonts
my_font = ('Times New Roman', 12)

# Defining Colors
root_color = '#6c1cbc'
button_color = '#e2cff4'

# Defining Functions
def add_item():
    """ Add individual item to ListBox """
    item = list_entry.get()
    if item != "":
        my_listbox.insert(tk.END, list_entry.get())
        list_entry.delete(0, tk.END)

def remove_item():
    """ Removes the selected item (Anchor) within the ListBox """
    my_listbox.delete(tk.ANCHOR)

def clear_list():
    """ Removes all the items within the ListBox """
    my_listbox.delete(0, tk.END)

def save_list():
    """ Saves all the items with the ListBox in a text file """
    with open(r'03. Simple Checklist\checklist.txt', 'w') as checklist:
        for item in my_listbox.get(0, tk.END):
            if item.endswith('\n'):
                checklist.write(item)
            else:
                checklist.write(item + '\n')

def open_list():
    """ Read all the items within Checklist.txt and prints on the ListBox """
    try:
        with open(r'03. Simple Checklist\checklist.txt', 'r') as checklist:
            for item in checklist:
                my_listbox.insert(tk.END, item)
    except:
        return


# Creating Root Window
root = tk.Tk(r'03. Simple Checklist\Assets\check.ico')
root.title('Simple Checklist')
root.iconbitmap(r'03. Simple Checklist\Assets\check.ico')
root.geometry('400x400+1400+300')
root.resizable(0, 0)
root.config(bg=root_color)

# DEFINE LAYOUTS
# Create Frames
input_frame = tk.Frame(root, bg=root_color)
output_frame = tk.Frame(root, bg=root_color)
button_frame = tk.Frame(root, bg=root_color)

input_frame.pack()
output_frame.pack()
button_frame.pack()

# Input Frame Layout
list_entry = tk.Entry(input_frame, width=35, borderwidth=3, font=my_font)
list_add_button = tk.Button(input_frame, text='Add Item', borderwidth=2, font=my_font, bg=button_color, command=add_item)

list_entry.grid(row=1, column=1, padx=5, pady=5)
list_add_button.grid(row=1, column=2, padx=5, pady=5, ipadx=5)

list_entry.focus_set()  # selected when the program runs

# Output Frame Layout
my_scorllbar = tk.Scrollbar(output_frame)
my_listbox = tk.Listbox(output_frame, width=45, height=15, borderwidth=3, font=my_font)

my_listbox.grid(row=1, column=1)
my_scorllbar.grid(row=1, column=2, sticky='ns')

my_scorllbar.config(command=my_listbox.yview)  # link the scroll bar with the list box
my_listbox.config(yscrollcommand=my_scorllbar.set)  # link scroll bar bar height with list box

# Button Frame Layout
list_remove_button = tk.Button(button_frame, text='Remove Item', font=my_font, bg=button_color, borderwidth=2, command=remove_item)
list_clear_button = tk.Button(button_frame, text='Clear List', font=my_font, bg=button_color, borderwidth=2, command=clear_list)
save_button = tk.Button(button_frame, text='Save List', font=my_font, bg=button_color, borderwidth=2, command=save_list)
quit_button = tk.Button(button_frame, text='Quit', font=my_font, bg=button_color, borderwidth=2)
quit_button.config(command=root.destroy)

list_remove_button.grid(row=1, column=1, padx=2, pady=7)
list_clear_button.grid(row=1, column=2, padx=2, pady=7, ipadx=10)
save_button.grid(row=1, column=3, padx=2, pady=7, ipadx=10)
quit_button.grid(row=1, column=4, padx=2, pady=7, ipadx=25)

# list_remove_button.pack(side=tk.LEFT, padx=2, pady=10)
# list_clear_button.pack(side=tk.LEFT, padx=2, pady=10, ipadx=10)
# save_button.pack(side=tk.LEFT, padx=2, pady=10, ipadx=10)
# quit_button.pack(side=tk.LEFT, padx=2, pady=10, ipadx=25)

# Open Checklist and show in the ListBox
open_list()

# Running Mainloop
root.mainloop()