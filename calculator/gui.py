"""
Graphical user interface for the simple calculator using tkinter.
"""

import tkinter as tk
from tkinter import messagebox
from .core import Calculator

class CalculatorGUI:
    """GUI implementation of the simple calculator."""
    
    def __init__(self, master):
        self.master = master
        master.title("Simple Calculator")
        self.calculator = Calculator()
        
        # Create UI elements
        self.create_widgets()
        
    def create_widgets(self):
        """Create and arrange all GUI components."""
        # Entry fields
        self.num1_entry = self.create_entry("First Number:", 0)
        self.num2_entry = self.create_entry("Second Number:", 1)
        
        # Operation buttons
        operations = [('+', 2), ('-', 3), ('*', 4), ('/', 5)]
        for text, row in operations:
            btn = tk.Button(
                self.master,
                text=text,
                width=5,
                command=lambda t=text: self.calculate(t)
            )
            btn.grid(row=row, column=1, pady=5)
        
        # Result display
        self.result_var = tk.StringVar()
        result_label = tk.Label(self.master, textvariable=self.result_var)
        result_label.grid(row=6, columnspan=2, pady=10)
        
        # History button
        history_btn = tk.Button(
            self.master,
            text="Show History",
            command=self.show_history
        )
        history_btn.grid(row=7, columnspan=2, pady=5)
        
    def create_entry(self, label_text, row):
        """Helper method to create labeled entry fields."""
        label = tk.Label(self.master, text=label_text)
        label.grid(row=row, column=0, padx=5, pady=5, sticky='e')
        
        entry = tk.Entry(self.master)
        entry.grid(row=row, column=1, padx=5, pady=5)
        return entry
    
    def calculate(self, operation):
        """Perform calculation based on the selected operation."""
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            
            if operation == '+':
                result = self.calculator.add(num1, num2)
            elif operation == '-':
                result = self.calculator.subtract(num1, num2)
            elif operation == '*':
                result = self.calculator.multiply(num1, num2)
            elif operation == '/':
                result = self.calculator.divide(num1, num2)
            
            self.result_var.set(f"Result: {result}")
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def show_history(self):
        """Display calculation history in a new window."""
        history_window = tk.Toplevel(self.master)
        history_window.title("Calculation History")
        
        history_text = tk.Text(history_window, width=40, height=10)
        history_text.pack(padx=10, pady=10)
        
        history = self.calculator.get_history()
        if not history:
            history_text.insert(tk.END, "No history available")
        else:
            for operation, result in history:
                history_text.insert(tk.END, f"{operation} = {result}\n")
        
        clear_btn = tk.Button(
            history_window,
            text="Clear History",
            command=lambda: [self.calculator.clear_history(), history_window.destroy()]
        )
        clear_btn.pack(pady=5)

def run_gui_calculator():
    """Run the calculator in GUI mode."""
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    run_gui_calculator()