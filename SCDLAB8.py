import tkinter as tk
from tkinter import messagebox

# Model - Calculator Logic
class CalculatorModel:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return num1 / num2


# View - GUI Interface
class CalculatorView:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("300x250")
        
        # Result display
        self.result_label = tk.Label(root, text="Result: ", font=("Arial", 14))
        self.result_label.pack(pady=10)
        
        # First number input
        tk.Label(root, text="First Number:").pack()
        self.entry1 = tk.Entry(root)
        self.entry1.pack(pady=5)
        
        # Second number input
        tk.Label(root, text="Second Number:").pack()
        self.entry2 = tk.Entry(root)
        self.entry2.pack(pady=5)
        
        # Operation buttons frame
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=15)
        
        # Buttons
        self.add_btn = tk.Button(self.button_frame, text="+", width=5, command=lambda: self.on_operation("add"))
        self.add_btn.grid(row=0, column=0, padx=2)
        
        self.sub_btn = tk.Button(self.button_frame, text="-", width=5, command=lambda: self.on_operation("subtract"))
        self.sub_btn.grid(row=0, column=1, padx=2)
        
        self.mul_btn = tk.Button(self.button_frame, text="*", width=5, command=lambda: self.on_operation("multiply"))
        self.mul_btn.grid(row=0, column=2, padx=2)
        
        self.div_btn = tk.Button(self.button_frame, text="/", width=5, command=lambda: self.on_operation("divide"))
        self.div_btn.grid(row=0, column=3, padx=2)
    
    def get_numbers(self):
        try:
            num1 = float(self.entry1.get())
            num2 = float(self.entry2.get())
            return num1, num2
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
            return None, None
    
    def set_result(self, result):
        self.result_label.config(text=f"Result: {result}")
    
    def on_operation(self, operation):
        return operation


# Controller - Coordinates Model and View
class CalculatorController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
    
    def calculate(self, operation):
        num1, num2 = self.view.get_numbers()
        
        if num1 is None and num2 is None:
            return
        
        try:
            if operation == "add":
                result = self.model.add(num1, num2)
            elif operation == "subtract":
                result = self.model.subtract(num1, num2)
            elif operation == "multiply":
                result = self.model.multiply(num1, num2)
            elif operation == "divide":
                result = self.model.divide(num1, num2)
            
            self.view.set_result(result)
        except ZeroDivisionError as e:
            messagebox.showerror("Error", str(e))


# Main Application
def main():
    root = tk.Tk()
    model = CalculatorModel()
    view = CalculatorView(root)
    controller = CalculatorController(model, view)
    
    # Connect buttons to controller
    view.add_btn.config(command=lambda: controller.calculate("add"))
    view.sub_btn.config(command=lambda: controller.calculate("subtract"))
    view.mul_btn.config(command=lambda: controller.calculate("multiply"))
    view.div_btn.config(command=lambda: controller.calculate("divide"))
    
    root.mainloop()


if __name__ == "__main__":
    main()
