import pytest

from ISBN import validate_isbn_10, validate_isbn_13, convert_isbn_10_to_isbn_13

def test_isbn_10():
    # Correct ISBN-10 number
    assert validate_isbn_10("0471958697") == True
    assert validate_isbn_10("0306406152") == True
    assert validate_isbn_10("0131103628") == True
    assert validate_isbn_10("076790818X") == True

    # Incorrect ISBN-10 number
    assert validate_isbn_10("032113354X") == False
    assert validate_isbn_10("013110362X") == False
    assert validate_isbn_10("030640615X") == False
    assert validate_isbn_10("0306406153") == False
    assert validate_isbn_10("0131103623") == False
    assert validate_isbn_10("0321133543") == False
    assert validate_isbn_10("0321197864") == False
    assert validate_isbn_10("0321200563") == False
    assert validate_isbn_10("030640615Y") == False
    assert validate_isbn_10("013110362Z") == False
    assert validate_isbn_10("ABCDEFGHIJ") == False
    assert validate_isbn_10("1234567890") == False
    assert validate_isbn_10("A12B34C56D") == False
    assert validate_isbn_10("X321133540") == False


def test_isbn_13():
    # Correct ISBN-13 number
    assert validate_isbn_13("9780895880468") == True
    assert validate_isbn_13("9780931988271") == True
    assert validate_isbn_13("9781861972712") == True
    assert validate_isbn_13("9783161484100") == True

    # Incorrect ISBN-13 number
    assert validate_isbn_13("978089588046a") == False
    assert validate_isbn_13("ABCDEFGHIJKLM") == False


def test_convert_isbn_10_to_isbn_13():
    # Correct ISBN-10 number
    assert convert_isbn_10_to_isbn_13("076790818X") =="9780767908184"
