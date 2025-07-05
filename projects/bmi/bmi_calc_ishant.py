import tkinter as tk
from tkinter import messagebox
import os

def calculate_bmi():
    name = entry_name.get()
    try:
        height = float(entry_height.get())
        weight = float(entry_weight.get())
        if weight <= 0 or height <= 0:
            messagebox.showerror("Input Error", "Enter values above 0!")
            return
        bmi = weight / (height ** 2)
        cat = category(bmi)
        
        result_text.set(f"BMI: {bmi:.2f}\nCategory: {cat}")
        save_file(name, height, weight, bmi, cat)
        messagebox.showinfo("Success", "Data successfully saved!")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter numeric values for height and weight.")

def category(bmi):
    if bmi <= 18.5:
        return "Underweight"
    elif 18.5 < bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def save_file(name, height, weight, bmi, category):
    with open(r"C:\Users\ishan\OneDrive\Desktop\upflair\projects\bmi\bmi_data.txt", 'a') as file:
        file.write(f"{name} | weight: {weight}kg | height: {height}m | bmi: {bmi:.2f} | category: {category}\n")

# GUI Setup
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x300")
root.resizable(False, False)

# Widgets
tk.Label(root, text="Enter your name:").pack(pady=2)
entry_name = tk.Entry(root)
entry_name.pack(pady=2)

tk.Label(root, text="Enter height (m):").pack(pady=2)
entry_height = tk.Entry(root)
entry_height.pack(pady=2)

tk.Label(root, text="Enter weight (kg):").pack(pady=2)
entry_weight = tk.Entry(root)
entry_weight.pack(pady=2)

tk.Button(root, text="Calculate BMI", command=calculate_bmi).pack(pady=10)

result_text = tk.StringVar()
tk.Label(root, textvariable=result_text, font=("Arial", 10, "bold")).pack(pady=5)

# Run app
root.mainloop()
