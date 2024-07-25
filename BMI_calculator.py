import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100  # Convert cm to meters
        if weight <= 0 or height <= 0:
            raise ValueError("Height and Weight must be positive numbers.")
        
        bmi = weight / (height ** 2)
        bmi_result_label.config(text=f"BMI: {bmi:.2f}")
        
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"
            
        bmi_category_label.config(text=f"Category: {category}")
    except ValueError as ve:
        messagebox.showerror("Input error", str(ve))
    except Exception as e:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers for weight and height.")

# Create the main window
window = tk.Tk()
window.title("Advanced BMI Calculator")

# Create and place the labels, entries, and buttons
tk.Label(window, text="Weight (kg):").grid(row=0, column=0, padx=10, pady=10)
weight_entry = tk.Entry(window)
weight_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(window, text="Height (cm):").grid(row=1, column=0, padx=10, pady=10)
height_entry = tk.Entry(window)
height_entry.grid(row=1, column=1, padx=10, pady=10)

calculate_button = tk.Button(window, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=2, columnspan=2, pady=10)

bmi_result_label = tk.Label(window, text="BMI: ")
bmi_result_label.grid(row=3, columnspan=2, pady=10)

bmi_category_label = tk.Label(window, text="Category: ")
bmi_category_label.grid(row=4, columnspan=2, pady=10)

# Run the main event loop
window.mainloop()
