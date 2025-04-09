import pytest
from calculator.core import Calculator

@pytest.fixture
def calc():
    return Calculator()

def test_add(calc):
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0
    assert calc.add(0, 0) == 0

def test_subtract(calc):
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(3, 5) == -2
    assert calc.subtract(0, 0) == 0

def test_multiply(calc):
    assert calc.multiply(2, 3) == 6
    assert calc.multiply(-1, 5) == -5
    assert calc.multiply(0, 10) == 0

def test_divide(calc):
    assert calc.divide(6, 3) == 2
    assert calc.divide(5, 2) == 2.5
    assert calc.divide(0, 1) == 0

def test_divide_by_zero(calc):
    assert calc.divide(5, 0) == "Error: Division by zero"

def test_history(calc):
    calc.add(2, 3)
    calc.subtract(5, 1)
    history = calc.get_history()
    assert len(history) == 2
    assert history[0][0] == "2 + 3"
    assert history[0][1] == 5
    assert history[1][0] == "5 - 1"
    assert history[1][1] == 4

def test_clear_history(calc):
    calc.add(1, 1)
    calc.clear_history()
    assert len(calc.get_history()) == 0