import pytest
from core.gf import GF

@pytest.fixture
def field():
    return GF(31)

@pytest.fixture
def elements(field):
    return field(13), field(19)

def test_addition(field, elements):
    x, y = elements
    assert x + y == field((13 + 19) % 31)

def test_subtraction(field, elements):
    x, y = elements
    assert x - y == field((13 - 19) % 31)
    assert y - x == field((19 - 13) % 31)

def test_multiplication(field, elements):
    x, y = elements
    assert x * y == field((13 * 19) % 31)

def test_division(field, elements):
    x, y = elements
    assert x / y == field((13 * pow(19, -1, 31)) % 31)
    assert y / x == field((19 * pow(13, -1, 31)) % 31)

def test_inverse(field, elements):
    x, y = elements
    assert (x / x) == field((13 * pow(13, -1, 31)) % 31)
    assert (y / y) == field((19 * pow(19, -1, 31)) % 31)

def test_exponentiation(field, elements):
    x, y = elements
    assert x ** 5 == field(pow(13, 5, 31))
    assert y ** 3 == field(pow(19, 3, 31))

def test_negation(field, elements):
    x, _ = elements
    assert -x == field((-13) % 31)

def test_mixed_operations(field):
    x = field(13)
    assert x + 3 == field((13 + 3) % 31)
    assert 3 + x == field((3 + 13) % 31)
    assert 7 * x == field((7 * 13) % 31)
    assert 1 / x == field((1 * pow(13, -1, 31)) % 31)

def test_bitwise_operations(field, elements):
    x, y = elements
    assert (x & y).value == (13 & 19) % 31
    assert (x | y).value == (13 | 19) % 31
    assert (x ^ y).value == (13 ^ 19) % 31
    assert (x << 1).value == (13 << 1) % 31
    assert (x >> 1).value == (13 >> 1)

def test_comparisons(field, elements):
    x, y = elements
    assert (13 < 19) == (x < y)
    assert (19 > 13) == (y > x)
    assert (13 <= 13) == (x <= x)
    assert (19 >= 19) == (y >= y)

def test_hash_and_equality(field, elements):
    x, y = elements
    assert x != y
    assert hash(x) == hash(field(13))
    assert x == field(13)

def test_casting(elements):
    x, _ = elements
    assert int(x) == 13
    assert bool(x)
    assert str(x) == "13"
