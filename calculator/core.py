"""
Core calculator operations and history management.
"""

import logging
from typing import Union, List, Tuple

# Set up logging for operation history
logging.basicConfig(
    filename='calculator_history.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

class Calculator:
    """A simple calculator with basic operations and history tracking."""
    
    def __init__(self):
        self.history: List[Tuple[str, Union[float, str]]] = []
    
    def add(self, a: float, b: float) -> float:
        """Return the sum of two numbers."""
        result = a + b
        self._log_operation(f"{a} + {b}", result)
        return result
    
    def subtract(self, a: float, b: float) -> float:
        """Return the difference between two numbers."""
        result = a - b
        self._log_operation(f"{a} - {b}", result)
        return result
    
    def multiply(self, a: float, b: float) -> float:
        """Return the product of two numbers."""
        result = a * b
        self._log_operation(f"{a} * {b}", result)
        return result
    
    def divide(self, a: float, b: float) -> Union[float, str]:
        """Return the quotient of two numbers or error message if dividing by zero."""
        try:
            result = a / b
            self._log_operation(f"{a} / {b}", result)
            return result
        except ZeroDivisionError:
            error_msg = "Error: Division by zero"
            self._log_operation(f"{a} / {b}", error_msg)
            return error_msg
    
    def _log_operation(self, operation: str, result: Union[float, str]) -> None:
        """Log the operation and result to history and file."""
        entry = (operation, result)
        self.history.append(entry)
        logging.info(f"{operation} = {result}")
    
    def get_history(self) -> List[Tuple[str, Union[float, str]]]:
        """Return the calculation history."""
        return self.history
    
    def clear_history(self) -> None:
        """Clear the calculation history."""
        self.history.clear()
        with open('calculator_history.log', 'w'):
            pass  # Clear the log file