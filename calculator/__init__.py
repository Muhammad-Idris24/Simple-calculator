"""
Simple Calculator package.

Provides both command-line and graphical calculator interfaces.
"""

from .core import Calculator
from .cli import run_cli_calculator
from .gui import run_gui_calculator

__version__ = "1.0.0"
__all__ = ['Calculator', 'run_cli_calculator', 'run_gui_calculator']