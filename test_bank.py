from bank import value

def test_value():
    assert value("здравствуйте") == "$0"
    assert value("здоров") == "$20"
    assert value("прив") == "$100"
