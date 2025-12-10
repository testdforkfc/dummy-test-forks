from src.calculator import Calculator

def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5

def test_multiply():
    calc = Calculator()
    assert calc.multiply(4, 5) == 20
