import pytest
from src.main import isEven, add, factorial

def test_add():
    assert add(2, 1) == 3
    assert add(-1, 1) == 0

def test_even():
    assert isEven(2) == True
    assert isEven(3) == False
    assert isEven(5) == False
    assert isEven(0) == True

def test_factorial_base_case():
    assert factorial(0) == 1

def test_factorial():
    assert factorial(5) == 120

def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-3)
