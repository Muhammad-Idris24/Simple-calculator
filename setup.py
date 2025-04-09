from setuptools import setup, find_packages

setup(
    name="simple_calculator",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'calculator-cli=calculator.cli:run_cli_calculator',
            'calculator-gui=calculator.gui:run_gui_calculator'
        ],
    },
    python_requires='>=3.6',
)