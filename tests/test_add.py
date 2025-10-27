import pytest
from math import isclose
from ScientificCalculator import ScientificCalculator

def test_add():
    calc = ScientificCalculator()
    assert calc.add(1, 2) == 3
    assert calc.add(-1, 2) == 1
    assert calc.add(0, 0) == 0

def test_subtract():
    calc = ScientificCalculator()
    assert calc.subtract(2, 1) == 1
    assert calc.subtract(-1, 2) == -3
    assert calc.subtract(0, 0) == 0

def test_multiply():
    calc = ScientificCalculator()
    assert calc.multiply(2, 3) == 6
    assert calc.multiply(-1, 2) == -2
    assert calc.multiply(0, 1) == 0

def test_divide():
    calc = ScientificCalculator()
    assert calc.divide(6, 2) == 3
    assert calc.divide(-4, 2) == -2
    with pytest.raises(ValueError):
        calc.divide(1, 0)

def test_sin():
    calc = ScientificCalculator()
    assert isclose(calc.sin(0), 0)
    assert isclose(calc.sin(3.14159/2), 1)

def test_cos():
    calc = ScientificCalculator()
    assert isclose(calc.cos(0), 1)
    assert isclose(calc.cos(3.14159), -1)

def test_tan():
    calc = ScientificCalculator()
    assert isclose(calc.tan(0), 0)
    assert isclose(calc.tan(3.14159), 0)

def test_sqrt():
    calc = ScientificCalculator()
    assert calc.sqrt(4) == 2
    assert calc.sqrt(0) == 0
    with pytest.raises(ValueError):
        calc.sqrt(-1)

def test_power():
    calc = ScientificCalculator()
    assert calc.power(2, 3) == 8
    assert calc.power(-2, 3) == -8
    assert calc.power(0, 1) == 0

def test_log():
    calc = ScientificCalculator()
    assert isclose(calc.log(1), 0)
    assert isclose(calc.log(2.71828), 1)
    with pytest.raises(ValueError):
        calc.log(-1)
    with pytest.raises(ValueError):
        calc.log(0)
    with pytest.raises(ValueError):
        calc.log(1, 1)
    with pytest.raises(ValueError):
        calc.log(1, -1)