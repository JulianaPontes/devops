from app import soma, subtrai, multiplica, divide
import pytest

def test_soma():
    assert soma(2, 3) == 5

def test_subtrai():
    assert subtrai(5, 3) == 2

def test_multiplica():
    assert multiplica(2, 4) == 8

def test_divide():
    assert divide(10, 2) == 5

def test_divide_por_zero():
    with pytest.raises(ValueError):
        divide(10, 0)