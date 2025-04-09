"""
Command-line interface for the simple calculator.
"""

from .core import Calculator

def run_cli_calculator():
    """Run the calculator in command-line interface mode."""
    calc = Calculator()
    print("Simple Calculator (Type 'quit' to exit)")
    
    while True:
        # Get user input
        try:
            num1 = input("Enter first number: ")
            if num1.lower() == 'quit':
                break
            
            num2 = input("Enter second number: ")
            if num2.lower() == 'quit':
                break
            
            operation = input("Choose operation (+, -, *, /): ")
            if operation.lower() == 'quit':
                break
            
            # Convert to float
            num1 = float(num1)
            num2 = float(num2)
            
            # Perform calculation
            if operation == '+':
                result = calc.add(num1, num2)
            elif operation == '-':
                result = calc.subtract(num1, num2)
            elif operation == '*':
                result = calc.multiply(num1, num2)
            elif operation == '/':
                result = calc.divide(num1, num2)
            else:
                print("Invalid operation. Please use +, -, *, or /")
                continue
            
            print(f"Result: {result}\n")
            
        except ValueError:
            print("Error: Please enter valid numbers\n")
        except KeyboardInterrupt:
            print("\nExiting calculator...")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}\n")

if __name__ == "__main__":
    run_cli_calculator()