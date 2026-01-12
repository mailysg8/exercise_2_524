import pytest
from pyos_pytest1.countchar import count_char

def test_count_char(): # check output is correct
    string = 'hello'
    expected = 5
    out = count_char.count_char(string)
    assert expected == out

    string = ''
    expected = 0
    out = count_char.count_char(string)
    assert expected == out

    string = 'hello class of 524'
    expected = 18
    out = count_char.count_char(string)
    assert expected == out

def test_count_char_wrong_input():
    with pytest.raises(TypeError): # check if it raises an error
        count_char.count_char(123)