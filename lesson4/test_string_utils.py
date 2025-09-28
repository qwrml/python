import pytest
from string_utils import StringUtils

string_utils = StringUtils()

# Тесты для функции capitalize()
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("test", "Test"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    (" ", " "),
    ("Already", "Already"),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

# Тесты для функции trim()
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("  hello", "hello"),
    (" test", "test"),
    ("string", "string"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    ("   ", ""),
    ("skypro   ", "skypro   "), 
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected

# Тесты для функции contains()
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("Skypro", "S", True),
    ("Skypro", "k", True),
    ("Hello World", " ", True),
    ("Python", "P", True),
    ("test", "t", True),
])
def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("Skypro", "U", False),
    ("Hello", "x", False),
    ("", "a", False),
    ("Test", "T", False),
    ("python", "P", False), 
])
def test_contains_negative(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected

# Тесты для функции delete_symbol()
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("Hello World", " ", "HelloWorld"),
    ("banana", "a", "bnn"),
    ("test", "t", "es"),
])
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("Skypro", "X", "Skypro"),
    ("Hello", "z", "Hello"),
    ("", "a", ""),
    ("Test", "test", "Test"), 
])
def test_delete_symbol_negative(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected