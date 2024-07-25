import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

def generate_password(length, use_uppercase, use_numbers, use_special_chars):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate():
    length = int(length_var.get())
    use_uppercase = use_uppercase_var.get()
    use_numbers = use_numbers_var.get()
    use_special_chars = use_special_chars_var.get()

    password = generate_password(length, use_uppercase, use_numbers, use_special_chars)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_to_clipboard():
    pyperclip.copy(password_entry.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Create main window
window = tk.Tk()
window.title("Password Generator")
window.geometry("400x300")

# Create and place widgets
tk.Label(window, text="Password Length:").grid(row=0, column=0, sticky='w', padx=10, pady=10)
length_var = tk.StringVar(value="12")
tk.Entry(window, textvariable=length_var, width=5).grid(row=0, column=1, padx=10, pady=10)

use_uppercase_var = tk.BooleanVar(value=True)
tk.Checkbutton(window, text="Include Uppercase", variable=use_uppercase_var).grid(row=1, columnspan=2, sticky='w', padx=10)

use_numbers_var = tk.BooleanVar(value=True)
tk.Checkbutton(window, text="Include Numbers", variable=use_numbers_var).grid(row=2, columnspan=2, sticky='w', padx=10)

use_special_chars_var = tk.BooleanVar(value=True)
tk.Checkbutton(window, text="Include Special Characters", variable=use_special_chars_var).grid(row=3, columnspan=2, sticky='w', padx=10)

tk.Button(window, text="Generate", command=generate).grid(row=4, columnspan=2, pady=10)

tk.Label(window, text="Generated Password:").grid(row=5, column=0, sticky='w', padx=10, pady=10)
password_entry = tk.Entry(window, width=30)
password_entry.grid(row=5, column=1, padx=10, pady=10)

tk.Button(window, text="Copy to Clipboard", command=copy_to_clipboard).grid(row=6, columnspan=2, pady=10)

# Run the main event loop
window.mainloop()
