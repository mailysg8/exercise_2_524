
import pytest
import pyos_pytest1 as pt1

@pytest.fixture
def einstein():
    with open('tests/einstein.txt', 'r') as f:
        content = f.read()
    return content


def test_count_char_fixture(einstein):
    # Test that count_char correctly counts the Einstein quote
    expected = 79  # Length of the quote including spaces and punctuation
    actual = pt1.count_char(einstein)
    assert actual == expected

def test_fixture_content(einstein):
    # Verify the fixture loaded the correct content
    assert "Insanity" in einstein
    assert "same thing over and over" in einstein
    
def test_count_char_with_fixture_word(einstein):
    # Test extracting and counting a word from the fixture
    word = einstein.split()[0]  # Gets "Insanity"
    expected = 8
    actual = pt1.count_char(word)
    assert actual == expected