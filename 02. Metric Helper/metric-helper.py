# Importing Libraries
import tkinter as tk
import tkinter.ttk as ttk

# Defining Fonts
field_font = ('Cambria', 10)

# Defining Colors
bg_color = '#c75c5c'
button_color = '#f5cf87'

# Defining Functions
def convert():
    global output_text
    """ Converts the value to the selected unit """
    metric_values = {
        'femto': 10**-15,
        'pico': 10**-12,
        'nano': 10**-9,
        'micro': 10**-6,
        'milli': 10**-3,
        'centi': 10**-2,
        'deci': 10**-1,
        'base value': 10**0,
        'deca': 10**1,
        'hecto': 10**2,
        'kilo': 10**3,
        'mega': 10**6,
        'giga': 10**9,
        'tera': 10**12,
        'peta': 10**15,
    }
    start_value = float(input_field.get())
    selected_input = input_combobox.get()
    selected_output = output_combobox.get()

    base_value = start_value * metric_values[selected_input]
    end_value = base_value / metric_values[selected_output]
    output_text.set(end_value)
    
def on_click(event):
    event.widget.delete(0, tk.END)


# Defining Root Window
root = tk.Tk()
root.title('Metric Helper')
root.iconbitmap(r'02. Metric Helper\Assets\ruler.ico')
root.resizable(0, 0)
root.config(bg=bg_color)

# Defining Layouts
input_text = tk.IntVar()
input_text.set('Enter your quantity')
output_text = tk.IntVar()
output_text.set(1)
input_field = tk.Entry(root, width=20, font=field_font, borderwidth=3, justify='center', textvariable=input_text)
output_field = tk.Label(root, width=20, font=field_font, borderwidth=3, textvariable=output_text)
equal_label = tk.Label(root, text='=', bg=bg_color)

input_field.bind("<Button-1>", on_click)

input_field.grid(row=1, column=1, padx=10, pady=10)
equal_label.grid(row=1, column=2, padx=10, pady=10)
output_field.grid(row=1, column=3, padx=10, pady=10)


# Creating ComboBox for Metric Values
metric_list = ['femto', 'pico', 'nano', 'micro', 'milli', 'centi', 'deci', 'base value', 'deca', 'hecto', 'kilo', 'mega', 'giga', 'tera', 'peta']

input_combobox = ttk.Combobox(root, value=metric_list, font=field_font, justify='center')
output_combobox = ttk.Combobox(root, value=metric_list, font=field_font, justify='center')
to_label = tk.Label(root, text='to', font=field_font, bg=bg_color)

input_combobox.grid(row=2, column=1, padx=10, pady=10)
to_label.grid(row=2, column=2, padx=10, pady=10)
output_combobox.grid(row=2, column=3, padx=10, pady=10)

input_combobox.set(metric_list[7])
output_combobox.set(metric_list[7])

# Conversion Button
convert_button = tk.Button(root, text='Convert', font=field_font, bg=button_color, command=convert)
convert_button.grid(row=3, column=1, columnspan=3, padx=10, pady=10, ipadx=50)

# Runnig Mainloop
root.mainloop()