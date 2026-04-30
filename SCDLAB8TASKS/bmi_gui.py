# bmi_gui.py
import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if height <= 0 or weight <= 0:
            messagebox.showerror("Error", "Height and weight must be greater than zero.")
            return

        # Calculate BMI
        bmi = weight / (height ** 2)
        category = ""

        # Logic to classify BMI
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi <= 24.9:
            category = "Normal"
        elif 25.0 <= bmi <= 29.9:
            category = "Overweight"
        else:
            category = "Obese"

        # Show the result along with category
        result_label.config(text=f"BMI: {bmi:.1f} ({category})")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numerical values.")

# Initialize main window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("250x250")

# Entry fields for height and weight
tk.Label(root, text="Weight (kg):").pack(pady=5)
weight_entry = tk.Entry(root)
weight_entry.pack()

tk.Label(root, text="Height (m):").pack(pady=5)
height_entry = tk.Entry(root)
height_entry.pack()

# Calculate button
calc_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calc_button.pack(pady=15)

# Result label
result_label = tk.Label(root, text="BMI: --", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

root.mainloop()