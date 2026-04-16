from app import soma, subtrai, multiplica, divide
import pytest


def test_soma():
    assert soma(2, 3) == 5


def test_subtrai():
    assert subtrai(10, 4) == 6


def test_multiplica():
    assert multiplica(3, 5) == 15


def test_divide():
    assert divide(8, 2) == 4


def test_divide_por_zero():
    with pytest.raises(ValueError):
        divide(10, 0)